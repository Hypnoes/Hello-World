#! python3

import time, sys

def progressBar():
    bar_length = 20
    for percent in range(0,101):
        hashs = u'\u25a0' * int(percent/100 * bar_length)
        spaces = u'\u25a1' * (bar_length - len(hashs))
        sys.stdout.write("\rPercent: [%s] %d%%"%(hashs + spaces, percent))
        sys.stdout.flush()
        time.sleep(0.25)
              
progressBar()
