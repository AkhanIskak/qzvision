''' Script file for work of cameras '''
from requests import post
import signal
import sys

from logger import logger
from camera import Camera
import config


camera = Camera(device=config.Vision.DEVICE.value,
                video=config.Vision.VIDEO.value)


def turn_off_handler(*_):
    ''' Turn off signal handler '''
    logger.info('Turning camera off')
    delta = camera.deactivate()

    post(
        url=config.Server.URL.value,
        json={
            'passengerAmount': delta,
            'routeId': config.Bus.ROUTE.value,
            'specificBusId': config.Bus.ID.value
        }
    )

    sys.exit(0)


def turn_on_handler():
    ''' Turning on cameras '''
    logger.info('Turning camera on')
    camera.activate()


signal.signal(signal.SIGTERM, turn_off_handler)

if __name__ == '__main__':
    turn_on_handler()
