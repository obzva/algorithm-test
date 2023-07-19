class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        n, m = len(word1), len(word2)
        w_i, i, w_j, j = 0, 0, 0, 0
        while w_i < n and w_j < m:
            word_i, word_j = word1[w_i], word2[w_j]
            char_i, char_j = word_i[i], word_j[j]
            if char_i != char_j:
                return False
            i += 1
            j += 1
            if i >= len(word_i):
                w_i += 1
                i = 0
            if j >= len(word_j):
                w_j += 1
                j = 0
        return w_i == n and w_j == m

            