# -*- coding: utf-8 -*-

a = list(input())
n = int(input())
c = []

if n < 0:
    print(-1)
    exit()

for i in range(len(a)):
    if not i+n > len(a):
        c.append(''.join(a[i:i+n]))

if not c:
    print(-1)
else:
    for i in c:
        print(i, end=' ')