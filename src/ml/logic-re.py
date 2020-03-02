import sys

from math import e

import numpy as np
from pylab import legend, scatter, plot, show, xlabel, ylabel


def main(a1):
    '''
        Load test dataset
    '''
    data = np.loadtxt(a1, delimiter=',')

    X = data[:, 0:2]
    Y = data[:, 2]

    pos = np.where(Y == 1)
    neg = np.where(Y == 0)

    scatter(X[pos, 0], X[pos, 1], marker='o', c='b')
    scatter(X[neg, 0], X[neg, 1], marker='x', c='r')

    xlabel("Featrue_1/Exam_1 score")
    ylabel("Featrue_2/Exam_2 score")
    legend(['Fail', 'Pass'])
    show()

def sigmod(X):
    '''Compute sigmod function'''
    den = 1.0 + e ** (-1.0 * X)
    gz = 1.0 / den
    return gz

def compute_cost(theta, X, Y):
    '''Compute cost given predicted and actual values'''
    m = X.shape[0]          # number of training examples
    theta = np.reshape(theta, (len(theta), 1))

    J = (1. / m) * (- np.transpose(Y).dot(np.log(sigmod(X.dot(theta)))) - np.transpose(1 - Y).dot(np.log(1 - sigmod(X.dot(theta)))))

    grad = np.transpose((1. / m) * np.transpose(sigmod(X.dot(theta)) - Y).dot(X))
    return J[0][0]

def compute_grad(theta, X, Y):
    '''compute gradient'''
    theta.shape = (1, 3)
    grad = np.zeros(3)
    h = sigmod(X.dot(theta.T))
    delta = h - Y
    l = grad.size
    m = X.shape[0]
    for i in range(l):
        sum_delta = delta.T.dot(X[:, i])
        grad[i] = (1. / m) * sum_delta * -1
    theta.shape(3, )
    return grad

if __name__ == '__main__':
    main(sys.argv[1])
