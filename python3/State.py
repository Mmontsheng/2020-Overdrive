import enum

class State(enum.Enum):
    ACCELERATING = "ACCELERATING"
    READY = "READY"
    NOTHING = "NOTHING"
    TURNING_RIGHT = "TURNING_RIGHT"
    TURNING_LEFT = "TURNING_LEFT"
    HIT_MUD = "HIT_MUD"

