from dataclasses import dataclass
from datetime import datetime


@dataclass
class ButtonEvent:
    pressed: bool
    dt: datetime


class PowerState:
    SCREEN_ON = 0
    SCREEN_OFF = 1
