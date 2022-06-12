# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 12:25
# @Author  : lys
# @Project : pythonProject
# @File    : 线程池.py

#.创建线程池ThreadPoolExecutor，提交任务submit()，查询状态done(),获取结果result()
# from concurrent.futures import ThreadPoolExecutor
# import time
# def get_html(times):
#     time.sleep(times)
#     print('{}, finished'.format(times))
#     return times
# executor = ThreadPoolExecutor(max_workers=2);   #创建线程池，传⼊max_workers参数来设置线程池中最多能同时运⾏的线程数⽬
# task1 = executor.submit(get_html, 3)      # 提交任务
# task2 = executor.submit(get_html, 2)
# print(task1.done())     # 查询任务状态，完成返回True,否则返回False
# print(task2.done())
# time.sleep(4)
# print(task1.done())
# print(task2.done())
# print(task1.result())      # 获取任务的返回值，注意：这个⽅法会阻塞主线程，等待这个任务执⾏完得到结果
# print(task2.result())
#
# if __name__ == '__main__':
#     pass




#循环等待任务执⾏完过程中如果某个线程抛出异常，则循环停⽌执⾏
#最终结果是一起都执行完一起返回的
#4. map()
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import time
# def get_html(times):
#     time.sleep(times)
#     return times
# executor = ThreadPoolExecutor(max_workers=2);   #创建线程池
# time_list = [5, 2, 4]
# for data in executor.map(get_html, time_list):
#     print(data)
# """
# 使⽤map⽅法，⽆需提前使⽤submit⽅法，map⽅法与python标准库中的map含义相同，都是将序列中的每个元素都执⾏同⼀个函数。这⾥是执⾏submit函数
# 上⾯的代码就是对time_list的每个元素都执⾏get_html函数，并分配给线程池。
# 可以看到执⾏结果与上⾯的as_completed⽅法的结果不同，输出顺序和time_list列表的顺序对应，就算2s的任务先执⾏完成，也会先打印出5s的任务先完成，再打印2s的任务完成。
# """
# if __name__ == '__main__':
#     pass


#3.as_completed()
#适合较多任务,可以不用分别列出start.和上面map()的区别是提前结束的会提前返回出结果,打印顺序根据执行完成的顺序
# ,map()则是等到列表中都完成再打印,并且顺序是列表顺序,不看执行快慢
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
def get_html(times):
    time.sleep(times)
    print('{}, finished'.format(times))
    return times
executor = ThreadPoolExecutor(max_workers=3);   #创建线程池
task1 = executor.submit(get_html, 5)      # 提交任务
task2 = executor.submit(get_html, 2)
for future in as_completed([task1, task2]):
    print(future.result())
#executor.shutdown(wait=True)
"""
    as_completed()⽅法是⼀个⽣成器，在没有任务完成的时候，会阻塞，在有某个任务完成的时候，会yield这个任务，就能执⾏for循环下⾯的语句，然后继续阻塞住，循环到所有的任务结束。
从结果也可以看出，先完成的任务会先通知主线程。
"""
if __name__ == '__main__':
    pass
