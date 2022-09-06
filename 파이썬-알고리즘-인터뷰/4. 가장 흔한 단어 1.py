"""
리스트 컴프리헨션, Counter 객체 사용
"""
import collections
import re
from typing import *


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # data cleansing
        words = [word for word in re.sub('[^\w]', '', paragraph)
        .lower().split()
                 if word not in banned]

        # USING DICTIONARY
        # # using defaultdict(), setting int as default value
        # counts = collections.defaultdict(int)
        # for word in words:
        #     counts[word] += 1
        #
        # # get max
        # return max(counts, key=counts.get)

        # EX: counts.most_common(1) = [('ball', 2)]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
