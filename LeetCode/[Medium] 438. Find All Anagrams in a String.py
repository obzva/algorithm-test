# My solution - single window with hash

# Time complexity: O(MN), iterate over M and in each iteration, iterate over N with check function
# Space complexity: O(MN), M N-sized hash


class Solution:
    def check(self, dict1, dict2):
        if len(dict1) != len(dict2):
            return False
        for key in dict1:
            if key not in dict2 or dict1[key] != dict2[key]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []

        p_dict = {}
        for char in p:
            if char not in p_dict:
                p_dict[char] = 0
            p_dict[char] += 1

        windows = [{} for _ in range(m - n + 1)]

        for i in range(n):
            char = s[i]
            if char not in windows[0]:
                windows[0][char] = 0
            windows[0][char] += 1

        answer = []
        if self.check(windows[0], p_dict):
            answer.append(0)

        for i in range(1, m - n + 1):
            for key in windows[i - 1]:
                windows[i][key] = windows[i - 1][key]

            windows[i][s[i - 1]] -= 1
            if windows[i][s[i - 1]] == 0:
                del windows[i][s[i - 1]]

            if s[i + n - 1] not in windows[i]:
                windows[i][s[i + n - 1]] = 0
            windows[i][s[i + n - 1]] += 1

            if self.check(windows[i], p_dict):
                answer.append(i)

        return answer


# More Pythonic way with Counter

# Time complexity: O(MN), iteration for M times and comparison takes O(N)
# Space complexity: O(N)

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []

        p_hash = Counter(p)
        s_hash = Counter()

        answer = []

        for i in range(m):
            s_hash[s[i]] += 1

            if i >= n:
                if s_hash[s[i - n]] == 1:
                    del s_hash[s[i - n]]
                else:
                    s_hash[s[i - n]] -= 1

            if p_hash == s_hash:
                answer.append(i - n + 1)

        return answer


# N is less than or equal to 26
