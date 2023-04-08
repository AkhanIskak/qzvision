''' Script file for work of cameras '''
import signal
import time
import sys

from logger import logger


def turn_off_handler(*_):
    ''' Turn off signal handler '''
    logger.info('Turning camera off')
    sys.exit(0)


def turn_on_handler():
    ''' Turning on cameras '''
    logger.info('Turning camera on')

    while True:
        time.sleep(1)


signal.signal(signal.SIGTERM, turn_off_handler)

if __name__ == '__main__':
    turn_on_handler()
