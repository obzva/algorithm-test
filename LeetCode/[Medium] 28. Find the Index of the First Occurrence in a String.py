class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # PYTHONIC
        # return haystack.index(needle) if needle in haystack else -1

        # ITERATIVE
        # if len(haystack) < len(needle):
        #     return -1
        # for i in range(len(haystack) - len(needle) + 1):
        #     for j in range(len(needle)):
        #         if haystack[i + j] != needle[j]:
        #             break
        #         if j == len(needle) - 1:
        #             return i
        # return -1

        # RABIN KARP, BUILT-IN HASH
        # hash_needle = hash(needle)
        # for i in range(len(haystack) - len(needle) + 1):
        #     if hash(haystack[i:i + len(needle)]) == hash_needle:
        #         return i
        # return -1

        # KNUTH MORRIS PRATT

        # TABULATING LPS(LONGEST PREFIX AND ALSO SUFFIX)
        lps = [0] * len(needle)
        prev_lps_index, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prev_lps_index]:
                lps[i] = prev_lps_index + 1
                prev_lps_index += 1
                i += 1
            elif prev_lps_index == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps_index = lps[prev_lps_index - 1]

        i = 0  # POINTER FOR HAYSTACK
        j = 0  # POINTER FOR NEEDLE
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1
