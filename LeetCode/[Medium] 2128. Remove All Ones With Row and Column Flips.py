class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        first_number = 0
        first_row = []
        for i, row in enumerate(grid):
            if i == 0:
                first_number = row[0]
                first_row = row
            else:
                if first_number != row[0]:
                    for i in range(len(row)):
                        if first_row[i] + row[i] != 1:
                            return False
                else:
                    for i in range(len(row)):
                        if first_row[i] - row[i] != 0:
                            return False
        return True

        # Time complexity
        ## iteration for each elements
        ### O(NM)

        # Space complexity
        ## need to remember the first row
        ### O(N)
