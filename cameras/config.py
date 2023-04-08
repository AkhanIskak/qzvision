''' Configuration file for bus cameras server '''
from configparser import ConfigParser
from enum import Enum


config = ConfigParser()
config.read('settings.ini')


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
    FILENAME: str = config.get('LOGS', 'FILENAME')
    LEVEL: int = int(config.get('LOGS', 'LEVEL'))
