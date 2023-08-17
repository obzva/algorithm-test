class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s) - k + 1):
            if len(s[i : i + k]) == len(set(s[i : i + k])):
                res += 1
        return res
