"""
collections.deque(), popleft() 사용
"""
import collections
from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop() != strs.popleft():
                return False

        return True
