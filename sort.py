#! python3
# -*- coding:utf-8 -*-
__Author__ =  'Hypnoes'

import random

def quicksort(a):
    i = 0
    j = a.length - 1
    key = a[0]
    while(j != i):
        if key > a[j]:
            swap(a[i], a[j])
        j -= 1
        if key < a[i]:
            swap(a[i], a[j])
        i += 1

def newSeq():
    a = []
    for i in range(200):
        a[i] = random.randint(0, 500)
        print(a[i])
    return a

def swap(i, j):
    t = i
    i = j
    t = j