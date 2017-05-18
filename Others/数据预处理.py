#-*-coding:utf-8-*-  
import csv
import sys
import math

def read(path):
    li = []
    with open(path) as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            li.append(row)
    return li

def writeSvm(path, li):
    with open(path, 'w') as svmfile:
        count = 1
        for i in li:
            svmfile.write("{0} ".format(count))
            k = 1
            for j in i:
                svmfile.write("{0}:{1} ".format(k, j))
                k += 1
            svmfile.write('\n')
            count += 1

def write(path, li):
    with open(path, 'w') as f:
        cvw = csv.writer(f)
        for x in li:
            cvw.writerow(x)
        

def extract(li):
    lo = []
    for i in li:
        t = []
        for j in i.values():
            if j != '-':
                t.append(float(j))
            else:
                t.append(0)
        lo.append(t)
    return lo

def trans(li):
    return map(list, zip(*li))

def cut(t, n = 96):
    b = []
    while len(t) >= n:
        o = [x for x in t[:n]]
        del t[:n]
        b.append(math.fsum(o)/len(o))
    return b

def reduction(li, n = 96):
    x = []
    for i in li:
        x.append(cut(i))
    return x

def main(input_file, output_file, mode='d'):
    li = read(input_file)
    for i in li:
        del i["时间"]
    li = extract(li)
    li = trans(li)
    li = reduction(li)
    write2(output_file, li)
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Input Error")
        print("py this.py <input_file> <output_file> [working_mode='default']")
    else:
        main(sys.argv[1], sys.argv[2], mode)
