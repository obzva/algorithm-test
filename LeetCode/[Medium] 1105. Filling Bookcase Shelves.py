class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        max_int = 1000 * n + 1
        dp = [max_int] * (n + 1)
        dp[0] = 0
        for i in range(n):
            j = i
            current_width = 0
            current_height = 0
            while j >= 0:
                current_width += books[j][0]
                if current_width > shelfWidth:
                    break
                current_height = max(current_height, books[j][1])
                dp[i + 1] = min(dp[i + 1], dp[j] + current_height)
                j -= 1
        return dp[-1]

        # Time complexity
        ## iteration -> O(N)
        ## nested iteration -> O(N) at worst
        ### O(N^2)

        # Space complexity
        ## dp -> O(N)
        ### O(N)
