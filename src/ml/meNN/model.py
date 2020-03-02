#!python3
# -*- coding: utf-8 -*-
__Author__ = 'Hypnoes'

import random
from typing import Callable, List, TypeVar

from vector import Vector
from itertools_ex import grouper

T = TypeVar('T')

class GenralDataType(object):
    '''
        GeneralDataType: General Data Type

        + this.feature: Vector
        + this.label: float
    '''
    def __init__(self, features: Vector, label: float, featurename: List[str] = None):
        self.features = features
        self.label = label

        self.featurename = featurename

    def get_feature(self, name: str) -> float:
        index = self.featurename.index(name)
        return self.features[index]

    def get_feature_len(self) -> int:
        return len(self.features)

    def __str__(self):
        return 'D'

    def __repr__(self):
        return 'D'

class Model(object):
    def __init__(self, fn: Callable, loss: Callable = None):
        self.fn = fn
        self.loss = loss

        self.W: Vector

    def fit(self, data: List[GenralDataType],
            lr: float,
            batch_size: int = 20,
            iteration: int = 1,
            epoch: int = 16) -> None:
        '''
            Training the model.

            `params`
                data: training data
                lr: Learning rate
                batch_size: batch size
                iteration: iteration
                epoch: epoch

            `return`
                None
        '''

        W_ = [0.0] * max(data, key=lambda x: x.get_feature_len) # fix len data[1]
        bias = 0.0
        y_ = 0.0

        batchs = grouper(data, batch_size)

        for i in range(epoch):
            err = 0.0
            for batch in batchs:
                for d in batch:
                    f = d.features
                    l = d.label


                    for _ in range(iteration):
                        # forward broadcast
                        for w, x in zip(W_, f):
                            y_ += w * x

                        y_ = self.fn(y_ + bias)

                        # backward broadcast
                        delta_W = list(map(lambda x_i: lr * (l - y_) * x_i, f))
                        delta_b = lr * (l - y_)
                        W_ = add(W_, delta_W)
                        bias += delta_b

                        err += (l - y_)

            print(f'epoch {i}: err -> {err}')

        self.W = W_

    def estimize(self, data: List[GenralDataType]) -> float:
        features = list()
        labels = list()

        for i in data:
            features.append(i.features)
            labels.append(i.label)

        y_ = list()
        for f in features:
            y = sum([w * x for w, x in zip(self.W, f)])
            y_.append(y)

        y_ = list(map(lambda i: 1.0 if i >= avg(y_) else 0.0, y_))

        acc = len(select(lambda t: t[0] == t[1], zip(y_, labels))) / len(data)

        return acc

def select(fn: Callable[..., bool], l: List[T]) -> List[T]:
    return [x for x in l if fn(x)]

def add(l1: Vector, l2: Vector) -> Vector:
    if len(l1) == len(l2):
        return list(map(sum, zip(l1, l2)))
    else:
        raise ValueError("Not in same dim.")

def avg(l: Vector) -> float:
    return sum(l) / len(l)

def sgn(x: float) -> float:
    return 1.0 if x > 0 else 0.0

def linear(x: float) -> float:
    return x

def splist(l: List[T], s: int) -> List[List[T]]:
    return [l[i:i+s] for i in range(len(l)) if i % s == 0]

def diff(fn: Callable, x: float, h: float) -> float:
    '''
        Differential.

        `paraments`
            fn : function
            x : point
            h : step

        `return`
            float
    '''
    return (-3 * fn(x - h) + 4 * fn(x) - fn(x + h)) / 2 * h

def gen_data(tri: int, tes: int) -> (Vector, Vector):
    '''
        Generate training and test data.

        `params`
            tri: number of training data
            tes: number of testing data

        `return`
            Tuple(train: Vector[GenralDataType], test: Vector[GenralDataType])

    '''

    c1x_train = list()
    c1y_train = list()
    c2x_train = list()
    c2y_train = list()

    c1x_test = list()
    c1y_test = list()
    c2x_test = list()
    c2y_test = list()

    train = list()
    test = list()

    # data structure : List(GenralDataType(features: List, label: Double))
    # train-data
    for i in range(tri):
        c1x_train.append(random.uniform(0.0, 0.5))
        c1y_train.append(random.uniform(0.0, 0.5))

        c2x_train.append(random.uniform(0.5, 1.0))
        c2y_train.append(random.uniform(0.5, 1.0))

        train.append(GenralDataType([c1x_train[i], c1y_train[i]], 0))
        train.append(GenralDataType([c2x_train[i], c2y_train[i]], 1))

    # test-data
    for i in range(tes):
        c1x_test.append(random.uniform(0.0, 0.5))
        c1y_test.append(random.uniform(0.0, 0.5))

        c2x_test.append(random.uniform(0.5, 1.0))
        c2y_test.append(random.uniform(0.5, 1.0))

        test.append(GenralDataType([c1x_test[i], c1y_test[i]], 0))
        test.append(GenralDataType([c2x_test[i], c2y_test[i]], 0))

    random.shuffle(train)
    random.shuffle(test)

    return train, test

def gen_data_(tri: int, tes: int) -> (Vector, Vector):
    '''
        Generate training and test data.

        `params`
            tri: number of training data
            tes: number of testing data

        `return`
            Tuple(train: Vector[GenralDataType], 
                test: Vector[GenralDataType])

    '''

    dataset = []
    for i in range(tri + tes):
        dataset.append(GenralDataType([random.uniform(0.0, 0.5), random.uniform(0.0, 0.5)], 0))
        dataset.append(GenralDataType([random.uniform(0.5, 1.0), random.uniform(0.5, 1.0)], 1))

    train = random.sample(dataset, tri)
    test = random.sample(dataset, tes)

    return train, test


def main():
    train, test = gen_data_(1000, 10)

    model = Model(linear)

    model.fit(train, 0.5, iteration=3)
    acc = model.estimize(test)

    print(f'acc: {acc}')

if __name__ == '__main__':
    main()
