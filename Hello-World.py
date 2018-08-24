#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
	Hello_World.py
'''
from functools import reduce

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        bdd = {}

        def f(x, y):
            if y in range(3):
                if x in range(3):
                    return 0
                elif x in range(3, 6):
                    return 1
                elif x in range(6, 9):
                    return 2
            elif y in range(3, 6):
                if x in range(3):
                    return 3
                elif x in range(3, 6):
                    return 4
                elif x in range(6, 9):
                    return 5
            elif y in range(6, 9):
                if x in range(3):
                    return 6
                elif x in range(3, 6):
                    return 7
                elif x in range(6, 9):
                    return 8
            else:
                return 9
        
        def g(xs):
            return len(xs) == len(set(xs)) and set(xs) <= set(range(10))

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    bdd[(i, j)] = int(board[i][j])

        for i in range(9):
            # line test
            if not g(list(map(bdd.get, [x for x in bdd.keys() if x[1] == i]))):
                print("line error.", i)
                return False
        
            # col test
            if not g(list(map(bdd.get, [x for x in bdd.keys() if x[0] == i]))):
                print("col error.", i)
                return False
            
            # block test
            if not g(list(map(bdd.get, [x for x in bdd.keys() if f(x[0], x[1]) == i]))):
                print("block error.", i)
                return False

        return True

def main():
    test = [["5","3",".",".","7",".",".",".","."],\
            ["6",".",".","1","9","5",".",".","."],\
            [".","9","8",".",".",".",".","6","."],\
            ["8",".",".",".","6",".",".",".","3"],\
            ["4",".",".","8",".","3",".",".","1"],\
            ["7",".",".",".","2",".",".",".","6"],\
            [".","6",".",".",".",".","2","8","."],\
            [".",".",".","4","1","9",".",".","5"],\
            [".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    print(solution.isValidSudoku(test))

if __name__ == '__main__':
    main()
