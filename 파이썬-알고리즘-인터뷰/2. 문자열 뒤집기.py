class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s = s[::-1] -> 공간 복잡도가 O(1)로 제한되어 있어서 리트코드에선 오류가 발생한다
        s[:] = s[::-1]
