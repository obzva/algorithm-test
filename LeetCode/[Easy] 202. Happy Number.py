class Solution:
    def isHappy(self, n: int) -> bool:
        # MY SOLUTION
        #
        # stack = [n]
        # while n != 1:
        #     tmp = 0
        #     while n:
        #         tmp += (n % 10) ** 2
        #         n //= 10
        #     if tmp in stack:
        #         return False
        #     stack.append(tmp)
        #     n = tmp
        # return True

        # OPTIMIZATION OF MY SOLUTION

        stack = [n]
        while n != 1:
            n = sum([int(x) ** 2 for x in str(n)])
            if n in stack:
                return False
            stack.append(n)
        return True
