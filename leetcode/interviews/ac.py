from itertools import zip_longest

a = input().split(' ')
b = input().split(' ')
c = []

for i in zip_longest(a, b, fillvalue=''):
    if i[0]:
        c.append(i[0]) 
    if i[1]:
        c.append(i[1])

for i in c:
    print(i, end=' ')
