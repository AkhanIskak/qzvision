''' Configuration file for bus cameras server '''
from configparser import ConfigParser
from enum import Enum
from os import path


config = ConfigParser()
config.read('settings.ini')


class Directory(Enum):
    ''' Class representing a directory configuration '''
    BASE = path.dirname(__file__)
    LOGS = path.join(BASE, 'logs')


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
