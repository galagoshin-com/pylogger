import os

import src.logger
import unittest
import time

def read_log(logfile: str) -> str:
    f = open(logfile, 'r')
    log_content = f.read()
    f.close()
    return log_content

class TestLogger(unittest.TestCase):
    def test_print(self):
        src.logger.logfiles.start_write_new_logfile()
        START_TIME1 = time.strftime("%Y.%m.%d %H:%M:%S")
        LOGFILE = f'{os.getenv("LOG_DIR")}/{START_TIME1}.log'
        src.logger.print('Hello world!')
        self.assertEqual(read_log(LOGFILE), f'[{START_TIME1}] > Hello world!\n')
        src.logger.print('Yet another message')
        START_TIME2 = time.strftime("%Y.%m.%d %H:%M:%S")
        self.assertEqual(read_log(LOGFILE), f'[{START_TIME1}] > Hello world!\n[{START_TIME2}] > Yet another message\n')

    def test_warning(self):
        src.logger.logfiles.start_write_new_logfile()
        START_TIME = time.strftime("%Y.%m.%d %H:%M:%S")
        LOGFILE = f'{os.getenv("LOG_DIR")}/{START_TIME}.log'
        src.logger.warning('Hello world!')
        self.assertEqual(read_log(LOGFILE), f'[{START_TIME}] WARNING > Hello world!\n')

    def test_error(self):
        src.logger.logfiles.start_write_new_logfile()
        START_TIME = time.strftime("%Y.%m.%d %H:%M:%S")
        LOGFILE = f'{os.getenv("LOG_DIR")}/{START_TIME}.log'
        src.logger.error('Hello world!')
        self.assertEqual(read_log(LOGFILE), f'[{START_TIME}] ERROR > Hello world!\n')

    def test_fatal(self):
        src.logger.logfiles.start_write_new_logfile()
        START_TIME = time.strftime("%Y.%m.%d %H:%M:%S")
        LOGFILE = f'{os.getenv("LOG_DIR")}/{START_TIME}.log'
        try:
            src.logger.fatal('Hello world!')
        except:
            pass
        self.assertEqual(read_log(LOGFILE), f'[{START_TIME}] FATAL > Hello world!\n')


if __name__ == '__main__':
    unittest.main()
