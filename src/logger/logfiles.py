import os
import time

LOGDIR = os.getenv('LOG_DIR') if os.getenv('LOG_DIR') != None else '/var/log/pylogger'
START_TIME = time.strftime("%Y.%m.%d %H:%M:%S")

def start_write_new_logfile():
    global LOGDIR, START_TIME
    old_logfile = f'{LOGDIR}/{START_TIME}.log'
    if os.path.isfile(old_logfile):
        os.remove(old_logfile)
    LOGDIR = os.getenv('LOG_DIR') if os.getenv('LOG_DIR') != None else '/var/log/pylogger'
    START_TIME = time.strftime("%Y.%m.%d %H:%M:%S")

def write_log(message: str):
    if not os.path.isdir(LOGDIR):
        os.mkdir(LOGDIR)
    pathlog = f'{LOGDIR}/{START_TIME}.log'
    f = open(pathlog, 'a')
    f.write(message + "\n")
    f.close()