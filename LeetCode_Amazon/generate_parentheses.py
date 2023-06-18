class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def recursive(prev: str, open_count: int, close_count: int) -> str:
            if open_count == 0 and close_count == 0:
                ans.append(prev)
                return
            if open_count:
                recursive(prev + "(", open_count - 1, close_count)
            if close_count and open_count < close_count:
                recursive(prev + ")", open_count, close_count - 1)

        recursive("", n, n)
        return ans
