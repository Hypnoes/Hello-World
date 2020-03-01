#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
	leetcode.py
'''
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        # unicode
        # A-Z: [\u0041 - \u005A]
        # a-z: [\u0061 - \u007A]
        # 0-9: [\u0030 - \u0039]

        def isWord(*args: List[str]) -> bool:
            for c in args:
                if '\u0041' <= c <= '\u005A' or\
                   '\u0061' <= c <= '\u007A' or\
                   '\u0030' <= c <= '\u0039':
                    continue
                else:
                    return False
            return True

        if not s:
            return True

        for i in range(len(s) // 2):
            if isWord(s[i], s[-1 - i]) and s[i].lower() is s[-1 - i].lower():
                continue
            elif isWord(s[i], s[-1 - i]):
                continue
            else:
                return False

        return True

    def singleNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in d:
            if d[i] == 1:
                return i

