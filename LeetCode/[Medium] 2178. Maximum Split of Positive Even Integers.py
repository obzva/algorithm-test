class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        if finalSum <= 4:
            return [finalSum]
        res = []
        even_number = 2
        remainder = finalSum
        while remainder > even_number * 2:
            res.append(even_number)
            remainder -= even_number
            even_number += 2
        res.append(remainder)
        return res

        # Time compexity
        ## iteration -> O(sqrt(N))
        ### O(sqrt(N))

        # Space complexity
        ### O(sqrt(N))
