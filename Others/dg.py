'''
    Data Generator
'''

from random import random

def co(x):
    return "%f,%f\n" % x

def main():
    d = []
    for i in range(20):
        d.append((random(), random()))

    with open("aout.txt", "w") as target:
        target.writelines(map(co, d))

if __name__ == '__main__':
    main()
