# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 0:36
# @Author  : lys
# @Project : pythonProject
# @File    : logging_par.py
import logging.handlers
import os



class Logger:
    def __init__(self, file_path, app_name):
        self.logger = self.init_logger(file_path, app_name)

    def init_logger(self, file_path, app_name):
        level = logging.DEBUG
        my_log = logging.getLogger()
        my_log.setLevel(level=level)
        log_format = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s')

        # print log to file
        time_file_handler = logging.handlers.TimedRotatingFileHandler(
            os.path.join(file_path, app_name + '.log'),
            when='D',
            interval=2,
            backupCount=180
        )
        time_file_handler.suffix = '%Y-%m-%d-%H-%M-%S.log'  # 按 秒
        time_file_handler.setLevel(level)
        time_file_handler.setFormatter(log_format)

        # print log to console
        console = logging.StreamHandler()
        console.setFormatter(log_format)
        console.setLevel(level)

        my_log.addHandler(time_file_handler)
        my_log.addHandler(console)
        return my_log

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def exception(self, message):
        self.logger.exception(message)


if __name__ == '__main__':
    import datetime
    LOG_FILE_PATH='./log/'
    file_name='monitor'
    log_total_path=LOG_FILE_PATH+file_name+'.log'
    if not os.path.exists(LOG_FILE_PATH):
        os.mkdir(LOG_FILE_PATH)
    with open(log_total_path,'w') as f:
        f.write('')
    logger = Logger(LOG_FILE_PATH, file_name)
    logger.info('application start at {}'.format(datetime.datetime.utcnow()))



    ##验证
    a = 'abc'
    try:
        int(a)
    except Exception as e:
        # logger.error(e)
        # 抛出的异常要用logger.exception来输出,主要是方便你在日志和控制台更方便的发现报错信息
        logger.exception(e)
