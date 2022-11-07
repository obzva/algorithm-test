import collections
from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return [x[0] for x in count.most_common(k)]
