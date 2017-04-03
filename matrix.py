import time
import tkinter as tk

window = tk.Tk()
window.title("正常矩阵乘法演示程序")
window.geometry('300x200')
tk.Label(window, text='矩阵乘法', font=('Arial', 20)).pack()


# 函数


def matrixMul(A, B):
    res = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    return res

def Reshape(a, row, colum, n):
    for i in range(0, row):
        for j in range(colum, n):
            a[i][j] = 0
    for i in range(row, n):
        for j in range(0, n):
            a[i][j] = 0
    return a

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
    C = matrixMul(A, B)
    end = time.time()
    print(end-start)
    print("用矩阵乘法求A*B所得的矩阵C为：")
    for i in range(0, s[0]):
        print(C[i][0:s[2]])

maopaobutton = tk.Button(window, text="矩阵乘法", command=main1).pack()
window.mainloop()
