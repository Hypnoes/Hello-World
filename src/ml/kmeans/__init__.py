from kmeans import KMeans

import numpy as np
import matplotlib.pyplot as plt

from random import uniform as r

def data_generator():
    neg = [f"{r(0, 0.5):.2f},{r(0, 0.5):.2f}\n" for _ in range(10)]
    pos = [f"{r(0.5, 1):.2f},{r(0.5, 1):.2f}\n" for _ in range(10)]
    with open("aout.txt", "w") as target:
        target.writelines(pos)
        target.writelines(neg)

def read_data(data_file: str) -> np.ndarray:
    data = []
    with open(data_file) as file:
        for line in file.readlines():
            data.append(line.rstrip("\n").split(","))

    return np.array(data, dtype=np.float)

def main():
    data = read_data('aout.txt')
    km = KMeans(2)

    g = km.fit(data)

    for i in g:
        plt.scatter(i[:, 0], i[:, 1])
    centers = np.array(km.centers)
    plt.scatter(centers[:, 0], centers[:, 1], c='m', marker='X', edgecolors='black')
    plt.savefig("kmeans-aout.png", bbox_inches="tight")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('end')
