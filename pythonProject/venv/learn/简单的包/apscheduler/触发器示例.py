# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 14:04
# @Author  : lys
# @Project : pythonProject
# @File    : date触发器，特定的时间点触发，作业任务只会执行一次.py




from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

def tick(ar):
    print('ar: ' +ar)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    #1. date触发器，特定的时间点触发，作业任务只会执行一次。
    # 在 2019-03-29 14:00:00 时刻运行一次 job_func 方法 args只能传一个字符串参数,不支持字典元组
    #其中，run_date赋值类型可以为date/datetime对象，或符合ISO_8601时间格式的字符串。其它时间格式及场景格式如下：
    #scheduler.add_job(tick, 'date', run_date=datetime(2022, 5, 18, 14, 22, 0), args=["text"])
    #datetime.date这个尝试不行
    #scheduler.add_job(tick, 'date', run_date=datetime.date(2022, 5, 18), args=['text'])
    #scheduler.add_job(tick, 'date', run_date='2022-05-18 14:24:25', args=['text'])
    #scheduler.add_job(tick, args=['text'])  # 立即运行

    #2）interval触发器，固定时间间隔触发。
    # 在 2019-03-29 14:00:01 ~ 2019-03-29 14:00:10 之间, 每隔两分钟执行一次job_func方法。
    #scheduler.add_job(tick, 'interval', minutes=2, start_date='2019-03-29 14:00:01', end_date='2019-03-29 14:00:10')
    # 持续定时触发
    #scheduler.add_job(tick, 'interval', hours=2)
    # 使用jitter参数，用于在执行时间中添加一个随机组件，用于多服务器场景中防止同时运行一个job的场景。此时将额外延迟[-120,+120]
    #scheduler.add_job(tick, 'interval', hours=1, jitter=120)

    #3）cron 触发器，在特定时间周期性地触发，和Linux crontab格式兼容。
    # python使用的cron与标准的cron有所区别, 他只有5位
    # 他直接去掉和秒并且最后一位不能使用? 需要使用 * 代替
    # 在2019-03-30 00:00:00之前，每周一到周五的5:30(am)触发
    #scheduler.add_job(tick, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2019-03-30')
    #其中，start_date和end_date赋值类型可以为date / datetime对象，或符合ISO_8601时间格式的字符串。其它时间格式及场景格式如下：
    # 在六月七月八月十一月十二月的第三个周五的0点1点2点3点执行
    #scheduler.add_job(tick, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
    # 使用标准crontab表达式
    #scheduler.add_job(tick, CronTrigger.from_crontab('0 0 1-15 may-aug *'))
    # 使用jitter参数，同上
    #scheduler.add_job(tick, 'cron', hour='*', jitter=120)

    scheduler.start()