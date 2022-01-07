import logging
from datetime import datetime
from os import getcwd, listdir
from os.path import abspath, isfile, join


def errorLoggingDecorator(f):
    def Wrapper(*args,**kargs):
        try:
            return f(*args,**kargs)
        except Exception as e:
            logging.error('에러 발생!!!!')
            logging.error(e)
            return False
    return Wrapper

def transToDate(date):
    #### 2020-00-00 00:00 ####

    # year and month
    year,month,day_time = date.split('-')

    # day and time
    day,time = day_time.split()

    # hour and min
    hour,min = time.split(':')

    return datetime(*list(map(int,[year,month,day,hour,min])))

def getCurPath():
    return abspath(getcwd())