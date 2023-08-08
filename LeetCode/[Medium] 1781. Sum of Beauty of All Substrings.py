# class Solution:
#     def beautySum(self, s: str) -> int:
#         ans = 0
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 sub_s = s[i : j + 1]
#                 cnt_sorted = collections.Counter(sub_s).most_common()
#                 most, least = cnt_sorted[0], cnt_sorted[-1]
#                 ans += most[1] - least[1]
#         return ans

#         # Time complexity:
#         ## iteration -> O(N^2)
#         ## constructing Counter -> O(N)
#         ## most_common method -> O(NlogN)
#         ### O(N^3logN)

#         # Space complexity
#         ## constructing Counter -> O(N)


class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq_table = [0] * 26
            for j in range(i, len(s)):
                freq_table[ord(s[j]) - 97] += 1
                ans += max(freq_table) - min(x for x in freq_table if x > 0)
        return ans

        # Time complexity:
        ## iteration -> O(N^2)
        ## max and min -> constant
        ### O(N^2)

        # Space complexity
        ## constructing Counter -> constant
        ### constant
