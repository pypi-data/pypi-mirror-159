import sys
from time import sleep

import click
import logging


@click.group()
def pi_touch_cli():
    """
    Entrypoint for `pi_touch`
    """


@pi_touch_cli.command()
@click.option("-ll", "--log-level", type=click.INT, default=logging.INFO)
@click.option(
    "-bl",
    "--brightness-level",
    type=click.INT,
    multiple=True,
    default=(50, 80, 100),
    help="Pass multiple values to cycle between",
)
@click.option(
    "-p",
    "--power-sec",
    type=click.FLOAT,
    default=0.5,
    help="When a button is held this many seconds, cycle power rather than brightness",
)
@click.option("-c", "--channel", type=click.INT, help="GPIO pin button is connected to")
def run_manager(log_level, brightness_level, power_sec, channel):
    from pi_touch.manager import BacklightManager
    from pi_touch.button import ScreenButton
    from pi_touch import logger

    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(log_level)
    manager = BacklightManager(
        brightness_levels=brightness_level, power_thresh_secs=power_sec
    )
    btn = ScreenButton(channel=channel)
    btn.add_callback(manager.handle_event)
    logger.debug(
        f"Running with brightness levels : {brightness_level}, power_sec: {power_sec}, channel: {channel}"
    )
    while 1:
        try:
            sleep(0.1)
        except KeyboardInterrupt:
            sys.exit(0)
