import tkinter as tk
import time
window = tk.Tk()
window.title("strassen演示程序")
window.geometry('300x200')
tk.Label(window, text='Strassen算法', font=('Arial', 20)).pack()


# 函数


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


# 重组矩阵的方法
def Merge(a11, a12, a21, a22, n):
    k = int(2 * n)
    a = [[[0] for i in range(k)] for i in range(k)]
    for i in range(0, n):
        for j in range(0, n):
            a[i][j] = a11[i][j]
            a[i][j + n] = a12[i][j]
            a[i + n][j] = a21[i][j]
            a[i + n][j + n] = a22[i][j]
    return a


# 矩阵加法
def Plus(f, g, n):
    h = [[[0] for i in range(n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            h[i][j] = f[i][j] + g[i][j]
    return h


# 矩阵减法
def Minus(f, g, n):
    h = [[[0] for i in range(n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            h[i][j] = f[i][j] - g[i][j]
    return h


# 矩阵Strassen乘法方法
def Strassen(a, b, n):
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

def Reshape(a, row, colum, n):
    for i in range(0, row):
        for j in range(colum, n):
            a[i][j] = 0
    for i in range(row, n):
        for j in range(0, n):
            a[i][j] = 0
    return a


# 主函数
def main1():
    s = []
    print("请您输入矩阵的矩阵A的行数:")
    s.append(int(input()))
    print("请输入矩阵A的列数：")
    s.append(int(input()))
    print("请输入矩阵B的列数：")
    s.append(int(input()))
    print("您输入的矩阵A是" + str(s[0]) + "*" + str(s[1]) + "矩阵" + "矩阵B是" + str(s[1]) + "*" + str(s[2]) + "矩阵")

    hangi = max(s)
    hang = 1
    while (hang < hangi):
        hang *= 2
    A = [[[0] for i in range(hang)] for i in range(hang)]
    B = [[[0] for i in range(hang)] for i in range(hang)]
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            print("请输入矩阵A的第" + str(i + 1) + "行" + str(j + 1) + "列元素")
            A[i][j] = int(input())
    print("输入矩阵B(从左向右从上到下依次输入数据之间以空格间隔):")
    for i in range(0, s[1]):
        for j in range(0, s[2]):
            print("请输入矩阵B的第" + str(i + 1) + "行" + str(j + 1) + "列元素")
            B[i][j] = int(input())
    print("您输入的矩阵A是" + str(s[0]) + "*" + str(s[1]) + "矩阵" + "矩阵B是" + str(s[1]) + "*" + str(s[2]) + "矩阵")
    print("您输入的矩阵A为:")
    for i in range(0, s[0]):
        print(A[i][0:s[1]])
    A = Reshape(A, s[0], s[1], hang)
    print("您输入的矩阵B为:")
    for i in range(0, s[1]):
        print(B[i][0:s[2]])
    B = Reshape(B, s[1], s[2], hang)
    start = time.time()
    C = Strassen(A, B, hang)
    end = time.time()
    print(end-start)
    print("用Strassen算法求A*B所得的矩阵C为：")
    for i in range(0, s[0]):
        print(C[i][0:s[2]])

maopaobutton = tk.Button(window, text="strassen算法", command=main1).pack()
window.mainloop()
