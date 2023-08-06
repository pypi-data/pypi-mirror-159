import logging

logger = logging.getLogger("pi_touch")
if len(logger.handlers) == 0:
    logger.addHandler(logging.NullHandler())
