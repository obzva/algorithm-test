"""
collections.defaultdict(list) 사용
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for str in strs:
            # defaultdict를 사용했기에 key 존재 여부를 체크하지 않아도 된다
            dict["".join(sorted(str))].append(str)

        return dict.values()
