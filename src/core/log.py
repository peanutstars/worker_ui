# import rclpy
from rclpy.logging import get_logger

class Log:
    Logger = get_logger("UI")
    
    @classmethod
    def info(cls, msg):
        cls.Logger.info(msg)
    
    @classmethod
    def warn(cls, msg):
        cls.Logger.warn(msg)
    
    @classmethod
    def error(cls, msg):
        cls.Logger.error(msg)