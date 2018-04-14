#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json

def main():
    tmp = 'tmp.json'
    if os.path.exists(tmp):
        os.remove(tmp)
    os.system("pip list -o --format=json >> " + tmp)
    with open(tmp) as f:
        o = list(map(lambda x: x['name'], json.load(f)))
    for x in o:
        os.system("pip install --upgrade " + x)
    os.remove(tmp)

if __name__ == '__main__':
    main()