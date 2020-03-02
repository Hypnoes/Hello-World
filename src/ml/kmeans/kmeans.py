#!python3
'''
    ...Kmeans...
'''

__Author__ = 'Hypnoes'

from typing import *

from functools import partial
from random import sample

import numpy as np


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
                min_distance = min(
                    distance, key=partial(np.linalg.norm, ord=2))
                ixs = [i_ for i_ in range(len(distance)) if
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
