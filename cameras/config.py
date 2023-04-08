''' Configuration file for bus cameras server '''
from configparser import ConfigParser
from enum import Enum


config = ConfigParser()
config.read('settings.ini')


class Bus(Enum):
    ''' Class representing a bus configuration '''
    ID: str = config.get('BUS', 'ID')
