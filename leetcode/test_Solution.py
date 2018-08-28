#!python3

import unittest
from leetcode import Solution

class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertEqual(Solution.isPalindrome("A man, a plan, a canal: Panama"), True)

    def test_singleNumber(self):
        self.assertEqual(Solution.singleNumber([4, 1, 2, 1, 2]), 4)

if __name__ == '__main__':
    unittest.main()
