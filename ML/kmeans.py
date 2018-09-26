#!python3
'''
    ...Kmeans...
'''

__Author__ = 'Hypnoes'

from functools import partial
from random import sample
from typing import List

import numpy as np
import matplotlib.pyplot as plt

class KMeans(object):
    def __init__(self, k: int):
        self.k = k
        self.centers = None

    def fit(self, data: np.ndarray) -> List[np.ndarray]:
        centers = sample(list(data), self.k)
        groups = []
        for i in range(10):
            groups = [[] for i in range(self.k)]
            for point in data:
                distance = [point - center for center in centers]
                min_distance = min(distance, key=partial(np.linalg.norm, ord=2))
                ixs = [i_ for i_ in range(len(distance)) if\
                    not (min_distance == distance[i_]).all()][0]
                groups[ixs].append(point)
            new_centers = []
            for group in groups:
                new_center = np.array(group).mean(axis=0)
                new_centers.append(new_center)
            centers = new_centers
            print(f'{i}. Center: {centers}')
        self.centers = centers
        groups = list(map(np.array, groups))
        return groups

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
    plt.show()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('end')
