#! python3
# -*- coding: utf-8 -*-
__Author__ = 'Hypnoes'

import threading
import time

class Timer(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        print('starting: '+self.name)
        self.print_time(self.name, self.counter, 5)
        print('exiting: '+self.name)
    
    def print_time(self, threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print('{NAME}:{TIME}'.format(NAME=threadName, TIME=time.ctime(time.time())))
            counter += -1

thread1 = Timer(1, 'Thread-1', 1)
thread2 = Timer(2, 'Thread-2', 2)

thread1.start()
thread2.start()

print('Exit Main Thread.')
