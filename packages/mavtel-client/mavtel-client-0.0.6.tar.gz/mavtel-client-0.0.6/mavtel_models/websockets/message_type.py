from enum import Enum


class WSMessageType(Enum):
    METRIC_UPDATE = 'METRIC_UPDATE'
    SUBSCRIBE = 'SUBSCRIBE'
    HEARTBEAT = 'HEARTBEAT'
