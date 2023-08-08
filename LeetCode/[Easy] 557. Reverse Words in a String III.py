class Solution:
    def reverseWords(self, s: str) -> str:
        ans, n, i, j = "", len(s), 0, 0
        while j < n:
            if s[j] != " ":
                j += 1
            else:
                ans += s[i:j][::-1] + " "
                i, j = j + 1, j + 1
        ans += s[i:j][::-1]
        return ans

    # Time complexity:
    ## iteration -> O(N)
    ### O(N)

    # Space complexity:
    ### constant
