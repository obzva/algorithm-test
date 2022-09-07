"""
투 포인터: 중앙을 중심으로 확장
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 해당사항 없을 때 빠르게 리턴
        if len(s) == 1 or s == s[::-1]:
            return s

        # 슬라이딩 윈도우 확장시키는 함수
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        result = ''
        for i in range(len(s) - 1):  # 윈도우의 시작 크기는 2, 3 인덱스를 끝까지 조사할 필요 없음
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result
