"""
itertools.permutation
"""

import itertools
from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
