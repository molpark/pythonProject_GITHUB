# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 9:11
# @Author  : lys
# @Project : pythonProject
# @File    : schedule_test.py


from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit) as e:
        print(e)