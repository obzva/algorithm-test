class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        i, j = 0, n - 1
        ans = 0
        head, tail = "", ""
        while i < j:
            head = head + text[i]
            tail = text[j] + tail
            if head == tail:
                ans += 2
                head = ""
                tail = ""
            i += 1
            j -= 1
        if (
            head != "" and tail != "" or i == j
        ):  # pivot word exists or pivot word is made of one character
            ans += 1
        return ans

        # Time complexity
        ## iteration -> O(N / 2)
        ### O(N / 2)

        # Space complexity
        ## head -> O(N / 2) at worst
        ## tail -> O(N / 2) at worst
        ### O(N)
