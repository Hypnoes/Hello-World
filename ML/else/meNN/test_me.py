import unittest
import me

class TestMethods(unittest.TestCase):

    def test_select(self):
        i = [-3, -2, -1, 0, 1, 2, 3]
        o = [1, 2, 3]
        self.assertEqual(me.select(lambda x: x > 0, i), o)

if __name__ == '__main__':
    unittest.main()
