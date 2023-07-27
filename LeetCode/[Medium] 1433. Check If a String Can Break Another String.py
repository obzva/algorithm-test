class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        array1, array2 = sorted(s1), sorted(s2)
        bigger = 0
        for i in range(n):
            if array1[i] > array2[i]:
                if bigger == 0:
                    bigger = 1
                elif bigger == 2:
                    return False
            elif array1[i] < array2[i]:
                if bigger == 0:
                    bigger = 2
                elif bigger == 1:
                    return False
        return True
