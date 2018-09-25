#!python3
'''
    ...
'''

__Author__ = 'Hypnoes'

from functools import partial
from random import sample

import numpy as np
import matplotlib.pyplot as plt

NDarray = np.ndarray

class draw(object):
    def __init__(self, func):
        self.__func = func
        self.__return = None

    def __call__(self, *args, **kwargs):
        draw_data = {}

        self.__return = self.__func(*args, **kwargs)

        scatter_data = np.array(draw_data['scatter_data'])
        plot_data = np.array(draw_data['plot_data'])

        plt.scatter(scatter_data[:, 0], scatter_data[:, 1])
        plt.plot(plot_data[:, 0], plot_data[:, 1], 'rx')
        plt.show()

        return self.__return

class KMeans(object):
    def __init__(self, k: int):
        self.k = k

    def fit(self, data: NDarray) -> None:
        center_points = sample(list(data), self.k)
        for center_point in center_points:
            i = 0
            new_center_point = center_point
            for _ in range(10):
                distance = [point - new_center_point for point in data]
                distance.sort(key=partial(np.linalg.norm, ord=2))
                group = distance[:len(distance) // self.k]
                move = np.array(group).mean(axis=0)
                print(f"{i}. Center: {new_center_point}, Move: {move}")
                new_center_point = new_center_point + move
                i += 1
            print()

def read_data(data_file: str) -> NDarray:
    data = []
    with open(data_file) as file:
        for line in file.readlines():
            data.append(line.rstrip("\n").split(","))

    return np.array(data, dtype=np.float)

def main():
    data = read_data('aout.txt')
    km = KMeans(2)

    km.fit(data)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('end')
