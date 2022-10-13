from typing import *


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        mod_nums = [lower - 1] + nums + [upper + 1]
        ans = []
        for i in range(1, len(mod_nums)):
            if mod_nums[i] - mod_nums[i - 1] != 1:
                start = mod_nums[i - 1] + 1
                end = mod_nums[i] - 1
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + '->' + str(end))
        return ans
                