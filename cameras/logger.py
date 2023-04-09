''' Module for configuring logging '''
import logging
import config


class Logger(logging.Logger):
    ''' Class representing configurated logging module '''
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(config.Logs.FILE.value)
    handler.setFormatter(formatter)

    def __init__(self):
        super().__init__(
            name='system-activity',
            level=config.Logs.LEVEL.value
        )

        self.addHandler(self.handler)


logger = Logger()
