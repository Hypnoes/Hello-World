'''
    UNIT TEST
'''

import random

import unittest
import model as me

class TestDataClass(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__setattr__(i, kwargs[i])
        self.attrs = len(kwargs)

    def __str__(self):
        f = lambda x: f'{x}={self.__getattribute__(x)}'
        d = self.__dir__()[: self.attrs]
        return f"Test_Object({', '.join(map(f, d))})"

    def __repr__(self):
        return self.__str__()

class TestMethods(unittest.TestCase):

    def test_select(self):
        i = [-3, -2, -1, 0, 1, 2, 3]
        o = [1, 2, 3]
        self.assertListEqual(me.select(lambda x: x > 0, i), o)

    def test_splist(self):
        test1 = [1, 2, 3, 4, 5, 6]
        o1 = [[1, 2, 3], [4, 5, 6]]
        o2 = [[1, 2], [3, 4], [5, 6]]
        self.assertListEqual(me.splist(test1, 3), o1)
        self.assertListEqual(me.splist(test1, 2), o2)

        test2 = []
        for _ in range(2000):
            test2.append(TestDataClass(attr1=random.randint(0, 9), attr2=random.randint(0, 9)))

        self.assertIsInstance(me.splist(test2, 4), list)


if __name__ == '__main__':
    unittest.main()
