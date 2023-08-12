import collections

# https://leetcode.com/problems/determine-if-two-strings-are-close/editorial/

# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if len(word1) != len(word2):
#             return False

#         cnt1 = collections.Counter(word1)
#         cnt2 = collections.Counter(word2)

#         if set(list(cnt1.keys())) != set(list(cnt2.keys())):
#             return False

#         cnt1_values = sorted(list(cnt1.values()))
#         cnt2_values = sorted(list(cnt2.values()))

#         for j in range(len(cnt1_values)):
#             if cnt1_values[j] != cnt2_values[j]:
#                 return False

#         return True

#         # Time complexity
#         ## constructing Counter -> O(2 * N)
#         ## constructing ket set -> O(2 * 26) at worst -> const
#         ## constructing value list and sorting -> O(2 * (26 + 26log26)) -> const
#         ## iteration -> O(26) -> const
#         ### O(N)

#         # Space complexity
#         ### const, because the max size of list and hashmap is 26


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1, freq2 = [0] * 26, [0] * 26
        for i in range(len(word1)):
            idx1, idx2 = ord(word1[i]) - 97, ord(word2[i]) - 97
            freq1[idx1] += 1
            freq2[idx2] += 1
        s_freq1, s_freq2 = sorted(freq1), sorted(freq2)
        for j in range(26):
            if (freq1[j] * freq2[j] == 0) and (freq1[j] != 0 or freq2[j] != 0):
                return False
            if s_freq1[j] != s_freq2[j]:
                return False
        return True

        # Time complexity
        ## constructing freq table -> const
        ## putting value into freq table -> O(N)
        ## sorting -> const
        ## iteration -> const
        ### O(N)

        # Space complexity
        ### const
