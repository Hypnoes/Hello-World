#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import system, remove
from os import path, devnull
from subprocess import run
from json import load
from operator import add
from functools import reduce

def main():
    tmp = 'tmp.json'
    if path.exists(tmp):
        remove(tmp)
    system("pip list -o --format=json >> " + tmp)
    with open(tmp) as f:
        o = map(lambda x: x['name'], load(f))
    length = reduce(add, map(lambda x: 1, o))
    indx = 1
    for x in o:
        print(f"[{index}/{length}]: {x}", end='\r')
        run(['pip', 'install', '--upgrade', x], stdout=os.devnull)
        indx += 1
    remove(tmp)

if __name__ == '__main__':
    main()
