import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # SLIDING WINDOW AND HASHMAP

        # if k == 0:
        #     return 0
        #
        # hashmap = {}
        # left = right = 0
        # answer = 0
        # while right < len(s):
        #     hashmap[s[right]] = right
        #     right += 1
        #     while len(hashmap) > k:
        #         if hashmap[s[left]] == left:
        #             del hashmap[s[left]]
        #         left += 1
        #     answer = max(answer, right - left)
        # return answer

        # SLIDING WINDOW AND ORDERED DICTIONARY
        if k == 0:
            return 0

        hashmap = collections.OrderedDict()
        left = right = 0
        answer = 0
        while right < len(s):
            char = s[right]
            if char in hashmap:
                del hashmap[char]
            hashmap[char] = right
            right += 1

            if len(hashmap) == k + 1:
                _, idx = hashmap.popitem(last=False)
                left = idx + 1
            answer = max(answer, right - left)
        return answer
