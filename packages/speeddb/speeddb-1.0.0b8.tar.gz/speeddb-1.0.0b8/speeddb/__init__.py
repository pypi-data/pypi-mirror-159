__version__ = '1.0.0b8'
__all__ = ['SpeedDBClient', 'SpeedDBDatabase', 'RunUDPServer']

from .SpeedDB import SpeedDBClient, SpeedDBDatabase
from .utils.server import RunUDPServer