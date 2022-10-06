from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def recursive(front_no: int, back_no: int, prev: str) -> None:
            if len(prev) == 2 * n:
                ans.append(prev)
                return
            if front_no < n:
                recursive(front_no + 1, back_no, prev + '(')
            if back_no < front_no:
                recursive(front_no, back_no + 1, prev + ')')

        recursive(1, 0, '(')
        return ans
