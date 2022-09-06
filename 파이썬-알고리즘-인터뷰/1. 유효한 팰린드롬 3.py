"""
슬라이싱 활용
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)  # \W = [^0-9a-zA-Z_] 이다. 즉, 언더바 '_'가 포함돼 있기 때문에 정규식 부분에 '\W'를 쓸 수 없음
        # 슬라이싱
        return s == s[::-1]
