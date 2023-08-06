from typing import Dict, Optional

from mavtel_models.websockets.message_type import WSMessageType
from mavtel_models.websockets.messages.base_message import BaseWSMessage


class SubscribeWSMessage(BaseWSMessage):
    type = WSMessageType.SUBSCRIBE
    metrics: Dict[str, Optional[float]]
