from typing import Any, Dict

from mavtel_models.websockets.messages.base_message import BaseWSMessage


class MetricsUpdateWSMessage(BaseWSMessage):
    name: str
    data: Dict[str, Any]
