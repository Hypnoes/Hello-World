'''
    用法:
        py randMatrix.py f => 生成两个矩阵数据文件mat1 mat2用于初始化
        py randMatrix.py d => 标准方法计算
        py randMatrix.py s => strassen算法计算
'''

#! python3
# -*- coding:utf-8 -*-

import random
import sys
import time

#功能函数
def newMat(name):
    '''生成200 x 200的随机整数矩阵'''
    with open(name, 'w') as f:
        for i in range(200):
            for j in range(200):
                f.write(str(random.randint(0,500))+' ')
            f.write('\n')

def readMat(name):
    '''从文件中读取矩阵'''
    a = []
    l = []
    with open(name, 'r') as f:
        for line in f:
            for i in line.split(' '):
                if (i != '\n'):
                    l.append(int(i))
            a.append(l)
            l = []
    return a

def toString(C):
    '''输出模式'''
    D = []
    for i in C:
        D.append(str(i) + '\n')
    return D

#计时器
def timmer(func):
    def wrapper(a, b, n):
        start = time.time()
        ans = func(a, b, n)
        end = time.time()
        print(end - start)
        return ans
    return wrapper

#常规乘法
@timmer
def mulit(A, B, n):
    '''矩阵的常规乘法'''
    res = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    return res

#矩阵Strassen乘法方法
# 分割矩阵
def Divide11(a, n):
    k = int(n / 2)
    a11 = [[[0] for i in range(k)] for j in range(k)]
    for i in range(0, k):
        for j in range(0, k):
            a11[i][j] = a[i][j]
    return a11


def Divide12(a, n):
    k = int(n / 2)
    a12 = [[[0] for i in range(k)] for i in range(k)]
    for i in range(0, k):
        for j in range(k, n):
            a12[i][j - k] = a[i][j]
    return a12


def Divide21(a, n):
    k = int(n / 2)
    a21 = [[[0] for i in range(k)] for i in range(k)]
    for i in range(k, n):
        for j in range(0, k):
            a21[i - k][j] = a[i][j]
    return a21


def Divide22(a, n):
    k = int(n / 2)
    a22 = [[[0] for i in range(k)] for i in range(k)]
    for i in range(k, n):
        for j in range(k, n):
            a22[i - k][j - k] = a[i][j]
    return a22


def Merge(a11, a12, a21, a22, n):
    '''重组矩阵的方法'''
    k = int(2 * n)
    a = [[[0] for i in range(k)] for i in range(k)]
    for i in range(0, n):
        for j in range(0, n):
            a[i][j] = a11[i][j]
            a[i][j + n] = a12[i][j]
            a[i + n][j] = a21[i][j]
            a[i + n][j + n] = a22[i][j]
    return a


def Plus(f, g, n):
    '''矩阵加法'''
    h = [[[0] for i in range(n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            h[i][j] = f[i][j] + g[i][j]
    return h


def Minus(f, g, n):
    '''矩阵减法'''
    h = [[[0] for i in range(n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            h[i][j] = f[i][j] - g[i][j]
    return h

@timmer
def Strassen(a, b, n):
    '''矩阵Strassen乘法方法'''
    k = n
    if k == 2:
        d = [[[0] for i in range(2)] for i in range(2)]
        d[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        d[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        d[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        d[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return d
    else:
        a11 = Divide11(a, n)
        a12 = Divide12(a, n)
        a21 = Divide21(a, n)
        a22 = Divide22(a, n)
        b11 = Divide11(b, n)
        b12 = Divide12(b, n)
        b21 = Divide21(b, n)
        b22 = Divide22(b, n)
        k = int(n / 2)
        m1 = Strassen(a11, Minus(b12, b22, k), k)
        m2 = Strassen(Plus(a11, a12, k), b22, k)
        m3 = Strassen(Plus(a21, a22, k), b11, k)
        m4 = Strassen(a22, Minus(b21, b11, k), k)
        m5 = Strassen(Plus(a11, a22, k), Plus(b11, b22, k), k)
        m6 = Strassen(Minus(a12, a22, k), Plus(b21, b22, k), k)
        m7 = Strassen(Minus(a11, a21, k), Plus(b11, b12, k), k)

        c11 = Plus(Minus(Plus(m5, m4, k), m2, k), m6, k)
        c12 = Plus(m1, m2, k)
        c21 = Plus(m3, m4, k)
        c22 = Minus(Minus(Plus(m5, m1, k), m3, k), m7, k)
        c = Merge(c11, c12, c21, c22, k)
        return c


#主函数
def main(args):
    if args == 'f':
        newMat("mat1")
        newMat("mat2")
    else:
        A = readMat('mat1')
        B = readMat('mat2')
        if args == 's':
            C = Strassen(A, B, 200)
        else:
            C = mulit(A, B, 0)
        with open('ans', 'w') as f:
            f.writelines(toString(C))            
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append('s')
    main(sys.argv[1])