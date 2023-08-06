from datetime import datetime
from typing import Callable
from threading import Thread
from .events import ButtonEvent
from .gpio import GPIO as _GPIO

GPIO = next(_GPIO)


class ScreenButton(object):
    """
    With a pullup resistor the input pin will read a high state when button is not pressed. Conversely,
    pulldown resistor will read a low state when button is not pressed
    """

    _listeners: list[Callable[[ButtonEvent], None]]

    def __init__(self, channel):
        self.channel = channel
        self._setup_pin()
        self._listeners = []

    def _setup_pin(self):
        GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(
            self.channel, GPIO.BOTH, callback=self.__internal_callback, bouncetime=25
        )

    def __internal_callback(self, *args, **kwargs):
        dt = datetime.utcnow()
        pressed = GPIO.input(self.channel)
        task = Thread(target=self._internal_callback, kwargs=dict(pressed=pressed, dt=dt))
        task.run()

    def _internal_callback(self, pressed, dt):
        """This maintains a single listener on GPIO and dispatches the same event across listeners"""
        event = ButtonEvent(pressed=pressed, dt=dt)
        for listener in self._listeners:
            listener(event)

    def add_callback(self, func: Callable[[ButtonEvent], None]):
        self._listeners.append(func)
