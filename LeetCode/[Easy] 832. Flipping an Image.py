from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        def converter(num):
            return num ^ 1

        for i in range(n):
            row = image[i]
            j, k = 0, n - 1
            while j < k:
                row[j], row[k] = converter(row[k]), converter(row[j])
                j += 1
                k -= 1
            if j == k:
                row[j] = converter(row[j])
        return image

        # Time complexity
        ## iteration i -> O(N)
        ## iteration j, k -> O(N / 2)
        ### O(N ^ 2)

        # Space complexity
        ### constant
