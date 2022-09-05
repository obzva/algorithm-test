class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in dict:
                dict[sorted_str].append(str)
            else:
                dict[sorted_str] = [str]
        return dict.values()
