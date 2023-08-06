_GPIO = None


def get_gpio():
    global _GPIO
    try:
        yield load_gpio()
    finally:
        try:
            _GPIO.cleanup()  # noqa
        except AttributeError:
            ...


def load_gpio():
    global _GPIO
    if _GPIO is not None:
        return _GPIO

    import RPi.GPIO as __GPIO

    __GPIO.setmode(__GPIO.BCM)  # noqa
    _GPIO = __GPIO
    return _GPIO


def __getattr__(name):
    if name == "GPIO":
        return get_gpio()
    else:
        raise AttributeError()
