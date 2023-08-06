from threading import Lock
from typing import Generic, TypeVar

from . import logger

T = TypeVar("T")


class ThreadSafeAttr(Generic[T]):
    def __init__(self, value: T = None):
        self.value = value
        self.lock = Lock()
        logger.debug(self.value)

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"
        setattr(owner, self.private_name, self.value)
        logger.debug(f"{self.private_name} - {self.value}")

    def __get__(self, obj, objtype=None):
        logger.debug(f"{self.private_name} - GET - await thread")
        with self.lock:
            return getattr(obj, self.private_name)

    def __set__(self, instance, value):
        logger.debug(f"{self.private_name} - SET - {value} - await thread")
        with self.lock:
            setattr(instance, self.private_name, value)
        logger.debug(f"{self.private_name} - SET - {value} - complete")

    def __iter__(self):
        with self.lock:
            return self.value

    def __next__(self):
        with self.lock:
            return next(self.value)


class SysfsAttr(Generic[T]):
    value: T

    def __init__(self, fp):
        self.fp = fp
        self.lock = Lock()
        logger.debug(f"{self.__class__} - {self.fp}")

    def __set_name__(self, owner, name):
        self.name = name
        logger.debug(f"{self.__class__} - {self.name}")

    def __get__(self, obj, objtype=None) -> T:
        logger.debug(f"{self.name} - GET - await thread")
        with self.lock:
            logger.debug(f"{self.name} - GET - await open")
            with open(self.fp, "rb") as sys_fs:
                result = int(sys_fs.read())
        logger.debug(f"{self.name} - GET - {result}")
        return result

    def __set__(self, instance, value: T):
        logger.debug(f"{self.name} - SET - await thread")
        with self.lock:
            with open(self.fp, "w") as sys_fs:
                sys_fs.write(str(value))
            logger.debug(f"{self.name} - SET - {value}")
