import enum



class BatchDataType(str, enum.Enum):
    INTERPOLATED = 'interpolated'
    RECORDED = 'recorded'

    @classmethod
    def get_dtype(cls, dtype: str) -> "BatchDataType":
        return cls(dtype.strip().lower())


class ChannelState(enum.IntEnum):
    CLOSED = 0
    CLOSING = 1
    OPENING = 2
    OPEN = 3


class ChannelPoolState(enum.IntEnum):
    CLOSED = 0
    CLOSING = 1
    OPEN = 2