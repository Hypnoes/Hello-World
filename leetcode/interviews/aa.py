#!python3

if __name__ == '__main__':
    a = list(bin(int(input()))[2:])
    b = []
    for i in range(len(a) - 1, -1, -2):
        if i == 0:
            b.append(a[i])
        else:
            b.append(a[i-1] + a[i])
    b.reverse()

    e = {'0': '0', '00': '0', '01': '1', '1': '1', '10': '2', '11': '3'}
    c = list(map(lambda x: e[''.join(x)], b))
    h = ''.join(c)
    print(h)
