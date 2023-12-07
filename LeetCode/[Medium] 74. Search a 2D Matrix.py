# Binary search - flatten 2d matrix to 1d array

# Time Complexity: O(log(MN))
# Space Complexity: const


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        length = m * n

        lo, hi = 0, length - 1
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            row, col = mid // n, mid % n

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                lo = mid + 1

            else:
                hi = mid - 1

        return False
