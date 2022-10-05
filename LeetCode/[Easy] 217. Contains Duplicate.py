import collections
from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = collections.Counter(nums)
        return 1 < max(check.values())
