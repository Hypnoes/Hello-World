'''
    Data Generator
'''

from random import uniform as r

def f(x):
    return "%f,%f\n" % x

def g(a=0, b=0):
    return r(a, b), r(a, b)

def main():
    d = []
    for i in range(10):
        d.append(g(b=0.5))

    for i in range(10):
        d.append(g(0.5, 1.0))

    with open("aout.txt", "w") as target:
        target.writelines(map(f, d))

if __name__ == '__main__':
    main()
