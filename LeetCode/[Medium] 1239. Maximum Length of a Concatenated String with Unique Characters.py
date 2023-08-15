# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         def helper(word):
#             bit = 0
#             for char in word:
#                 new_bit = 1 << (ord(char) - 97)
#                 if bit ^ new_bit != bit | new_bit:
#                     return (0, 0)
#                 bit = bit | new_bit
#             return (len(word), bit)

#         tmp = [(0, 0)]
#         best = 0
#         for word in arr:
#             (n, bit_n) = helper(word)
#             if bit_n == 0:
#                 continue
#             for i in range(len(tmp)):
#                 (m, bit_m) = tmp[i]
#                 if bit_n | bit_m == bit_n ^ bit_m:
#                     tmp.append((m + n, bit_n | bit_m))
#                     best = max(best, m + n)
#         return best

#     # Time complexity
#     ## helper -> O(L) for word length L
#     ## iteration -> O(2**N)
#     ### O((2**N) * L)

#     # Space complexity
#     ### O(2**N) at worst


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)

        def helper(word):
            bit = 0
            for char in word:
                new_bit = 1 << (ord(char) - 97)
                if bit ^ new_bit != bit | new_bit:
                    return (0, 0)
                bit = bit | new_bit
            return (len(word), bit)

        def dfs(pos, bitmap, prev):
            best = prev
            for i in range(pos, n):
                (m, bit_m) = helper(arr[i])
                if bit_m == 0:
                    continue
                if bitmap | bit_m == bitmap ^ bit_m:
                    best = max(best, dfs(i + 1, bitmap | bit_m, prev + m))
            return best

        return dfs(0, 0, 0)

        # Time complexity
        ## helper -> O(L) for word length L
        ## iteration -> O(2**N)
        ### O((2**N) * L)

        # Space complexity
        ## recursion -> O(N) at deepest
        ### O(N)
