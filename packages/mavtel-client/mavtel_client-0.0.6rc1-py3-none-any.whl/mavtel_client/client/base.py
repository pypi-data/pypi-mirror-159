import logging
from typing import Optional, Set, Union
from urllib.parse import urljoin, urlparse

import httpx
import orjson
import websockets
from websockets.exceptions import ConnectionClosed

from mavtel_models import MAVLinkMetricBaseModel, SubscribeWSMessage, MetricsUpdateWSMessage
from mavtel_models import get_supported_metrics, parse_ws_message

log = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 50


class MAVTelClientBase:
    def __init__(self, url: str):
        self._url: str = url
        self._api_url = urljoin(self._url, 'api/v1')
        self._supported_metrics = get_supported_metrics()

    @property
    def url(self) -> str:
        return self._url

    def get_metric_url(self, metric: Union[MAVLinkMetricBaseModel.__class__, str]) -> str:
        metric_name = metric if isinstance(metric, str) else metric.get_metric_name()
        return f'{self._api_url}/metrics/{metric_name}'

    def get_metric_updates_ws_url(self) -> str:
        parsed_url = urlparse(self._url)
        ws_base_url = parsed_url._replace(scheme='ws').geturl()
        return urljoin(ws_base_url, 'api/v1/streams/metrics')

    async def healthcheck(self) -> bool:
        url = urljoin(self._url, 'health/check')
        async with httpx.AsyncClient() as client:
            try:
                response: httpx.Response = await client.get(url)
                return response.status_code == 200 and response.text == 'OK'
            except httpx.ConnectError:
                return False

    async def get_metric_by_class(
            self,
            metric_class: MAVLinkMetricBaseModel.__class__
    ) -> Optional[MAVLinkMetricBaseModel]:
        url = self.get_metric_url(metric_class)
        async with httpx.AsyncClient() as client:
            response: httpx.Response = await client.get(url, timeout=DEFAULT_TIMEOUT)
            data = orjson.loads(response.text)
            if data is None:
                return None
            return metric_class(**data)

    async def metric_updates(self, metric_names: Set[str] = None):
        metric_names = metric_names or set(self._supported_metrics.keys())
        if len(metric_names.difference(self._supported_metrics)) > 0:
            raise KeyError(f'Metrics {", ".join(metric_names.difference(self._supported_metrics))} are not supported!')

        async with websockets.connect(self.get_metric_updates_ws_url()) as websocket:
            subscribe_msg = SubscribeWSMessage(
                metrics={name: None for name in metric_names}
            ).json()
            await websocket.send(subscribe_msg)

            while True:
                try:
                    raw_message = await websocket.recv()
                    # noinspection PyTypeChecker
                    message: MetricsUpdateWSMessage = parse_ws_message(raw_message)

                    if not isinstance(message, MetricsUpdateWSMessage):
                        continue

                    metric_class: MAVLinkMetricBaseModel.__class__ = self._supported_metrics[message.name]

                    yield metric_class(**message.data)
                except orjson.JSONDecodeError as json_error:
                    log.error(f"Error decoding metrics message: {json_error}. Message: '{raw_message}'")
                except ConnectionClosed:
                    log.error(f'Websocket connection closed')
                    break
