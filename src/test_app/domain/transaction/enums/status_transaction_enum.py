from enum import Enum


class StatusTransactionEnum(str, Enum):
    OPEN = "open"
    CANCEL = "rollback"
    CLOSE = "close"
