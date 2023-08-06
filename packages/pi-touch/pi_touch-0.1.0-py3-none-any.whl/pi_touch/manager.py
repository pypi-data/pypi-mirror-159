from itertools import cycle
from pathlib import Path
from typing import Iterable, Optional

from . import logger
from .events import ButtonEvent, PowerState
from .utils import SysfsAttr, ThreadSafeAttr


class BacklightManager:
    BL_DIR = Path("/") / "sys" / "class" / "backlight" / "rpi_backlight"
    BL_POWER = BL_DIR / "bl_power"
    BL_BRIGHTNESS = BL_DIR / "brightness"
    MAX_BRIGHTNESS = 200

    power_state = SysfsAttr[PowerState](fp=BL_POWER)
    brightness_state = SysfsAttr[int](fp=BL_BRIGHTNESS)
    brightness_steps = ThreadSafeAttr[Optional[Iterable[int]]]()
    last_event = ThreadSafeAttr[Optional[ButtonEvent]]()

    """
    Manages RPI Backlight

    Attributes
    ----------
    BL_DIR : Path
        sysfs path to backlight device
    BL_POWER : Path
        sysfs path to backlight power state
    BL_BRIGHTNESS : Path
        sysfs path to backlight brightness
    MAX_BRIGHTNESS : int
        Maximum allowable brightness

    Notes
    -----

    Create a file with below contents at '/etc/udev/rules.d/XX-somerule.rules' where 'XX' is numeric.

    SUBSYSTEM="backlight",RUN+="/bin/chmod 666 /sys/class/backlight/%k/brightness /sys/class/backlight/%k/bl_power"

    This is necessary to avoid using `sudo` for changing brightness/power

    """

    def __init__(
        self,
        brightness_levels: Iterable[int] = (50, 80, 100),
        power_thresh_secs: float = 0.5,
    ):
        """

        Parameters
        ----------
        brightness_levels : Iterable[int]
            Cycle brightness levels
        power_thresh_secs : int | float
            When button is pressed and released for this number of seconds, cycle power state instead of brightness
        """
        self.brightness_steps = cycle(sorted(brightness_levels))
        self.power_thresh_secs = power_thresh_secs

    def handle_event(self, event: ButtonEvent):
        """
        Handle a button press event. If event is a button press - await a button release, otherwise proceed
        """

        # A button press should have a press and release
        logger.debug(f"handle_event: {event}")
        if event.pressed:
            self.last_event = event
            return

        # Ensure we have an event
        if not self.last_event:
            logger.warning(f"No previous button press found - synthesizing event")
            last_event = ButtonEvent(pressed=False, dt=event.dt)
        else:
            last_event = self.last_event
            self.last_event = None

        # Based on duration of press we trigger brightness step or power
        event_duration = (event.dt - last_event.dt).total_seconds()

        dur_meets_threshold = event_duration >= self.power_thresh_secs
        if dur_meets_threshold:
            logger.debug(f"Event has duration {event_duration} - Toggling Power")
            power_current = self.power_state
            power_new = (
                PowerState.SCREEN_ON
                if power_current == PowerState.SCREEN_OFF
                else PowerState.SCREEN_OFF
            )
            logger.info(
                f"Setting Backlight Power : {'On' if power_new == PowerState.SCREEN_ON else 'Off'}"
            )
            self.power_state = power_new
            return

        logger.debug(f"Event has duration {event_duration} - Cycling Brightness")
        next_brightness = next(self.brightness_steps)
        logger.info(f"Setting brightness to {next_brightness}")

        # We ensure power_state is on - no need to read and check
        self.brightness_state = next_brightness
        self.power_state = PowerState.SCREEN_ON
