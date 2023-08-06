from pydantic import BaseModel

from mavtel_models.websockets.message_type import WSMessageType


class BaseWSMessage(BaseModel):
    type: WSMessageType
