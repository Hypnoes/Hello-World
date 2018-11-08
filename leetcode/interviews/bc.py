from collections import Counter

a = list(input())
b = Counter(a)
c, d = b.most_common(2)
for i in range(len(a)):
    if a[i] == d[0]:
        a[i] = c[0]

e = Counter(a)
g = sum(map(lambda x: x * x, e.values()))
print(g)