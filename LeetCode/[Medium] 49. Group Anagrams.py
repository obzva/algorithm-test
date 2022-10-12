import collections
from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic = {}
        dic = collections.defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # if sorted_word not in dic:
            #     dic[sorted_word] = [word]
            # else:
            #     dic[sorted_word].append(word)
            dic[sorted_word].append(word)
        return list(dic.values())
