from typing import Any, Dict, Union

import orjson

from mavtel_models.websockets.message_type import WSMessageType
from mavtel_models.websockets.messages.base_message import BaseWSMessage
from mavtel_models.websockets.messages.heartbeat import HeartbeatWSMessage
from mavtel_models.websockets.messages.metric_update import MetricsUpdateWSMessage
from mavtel_models.websockets.messages.subscribe import SubscribeWSMessage


def get_ws_message_classes() -> Dict[WSMessageType, BaseWSMessage.__class__]:
    return {
        WSMessageType.HEARTBEAT: HeartbeatWSMessage,
        WSMessageType.METRIC_UPDATE: MetricsUpdateWSMessage,
        WSMessageType.SUBSCRIBE: SubscribeWSMessage,
    }


def parse_ws_message(data: Union[str, Dict[str, Any]]) -> BaseWSMessage:
    data: Dict[str, Any] = orjson.loads(data) if isinstance(data, str) else data

    message_type = WSMessageType(data['type'])

    return get_ws_message_classes()[message_type](**data)
