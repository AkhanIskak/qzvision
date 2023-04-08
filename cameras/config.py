''' Configuration file for bus cameras server '''
from configparser import ConfigParser
from typing import List
from enum import Enum
from os import path


config = ConfigParser()
config.read('settings.ini')


class Directory(Enum):
    ''' Class representing a directory configuration '''
    BASE = path.dirname(__file__)
    LOGS = path.join(BASE, 'logs')
    DATA = path.join(BASE, 'data')


class Bus(Enum):
    ''' Class representing a bus configuration '''
    ID: str = config.get('BUS', 'ID')


class Server(Enum):
    ''' Class representing a server configuration '''
    HOST: str = config.get('SERVER', 'HOST')
    PORT: int = int(config.get('SERVER', 'PORT'))
    DEBUG: bool = config.get('SERVER', 'DEBUG') == 'True'


class Logs(Enum):
    ''' Class representing logs configuration '''
    LEVEL: int = int(config.get('LOGS', 'LEVEL'))
    FILE: str = path.join(
        Directory.LOGS.value, config.get('LOGS', 'FILENAME'))


class Vision(Enum):
    ''' Class representing vision algorithm's configuration '''
    MODEL: str = path.join(Directory.DATA.value, config.get('DATA', 'MODEL'))
    INFO: str = path.join(Directory.DATA.value, config.get('DATA', 'INFO'))

    CONFIDENCE: float = float(config.get('VISION', 'CONFIDENCE'))
    SKIP_FRAMES: int = int(config.get('VISION', 'SKIP-FRAMES'))
    SCALE_FACTOR: float = float(config.get('VISION', 'SCALE-FACTOR'))
    MEAN: float = float(config.get('VISION', 'MEAN'))

    CLASSES: List[str] = ['background', 'aeroplane', 'bicycle', 'bird', 'boat',
                          'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
                          'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep',
                          'sofa', 'train', 'tvmonitor']


class Status(Enum):
    WAITING: str = 'Waiting'
    DETECTING: str = 'Detecting'
    TRACKING: str = 'Tracking'
