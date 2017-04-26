'''
    MODULE DOC
'''

#! python3
# -*- coding:utf-8 -*-
__Author__ = "Hypnoes"

import threading
import time
import sys

class Bar(threading.Thread):
    def __init__(self, threadID, threadName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName

    def run(self):
        self.progressBar()

    def progressBar(self):
        bar_length = 20
        for percent in range(0, 101):
            hashs = u'\u25a0' * int(percent/100 * bar_length)
            spaces = u'\u25a1' * (bar_length - len(hashs))
            sys.stdout.write("\rPercent: [%s] %d%%"%(hashs + spaces, percent))
            sys.stdout.flush()
            time.sleep(0.25)

def main():
    thread1 = Bar(1, "Bar-1")
    thread1.start()

if __name__ == '__main__':
    main()
