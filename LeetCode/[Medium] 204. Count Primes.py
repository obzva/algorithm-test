class Solution:

    def countPrimes(self, n: int) -> int:
        # MY SOLUTION - TIME LIMIT EXCEED
        # primes = []
        # def is_prime(num: int):
        #     if num == 1:
        #         return
        #     nonlocal primes
        #     if num == 2:
        #         primes.append(num)
        #         return
        #     for prime in primes:
        #         if num % prime == 0:
        #             return
        #     primes.append(num)
        #
        # for i in range(1, n):
        #     is_prime(i)
        # return len(primes)

        # SIEVE OF ERATOSTHENES
        if n <= 2:
            return 0
        ans = 0
        memo = [False] * n
        for i in range(2, n):
            if memo[i]:
                continue
            ans += 1
            j = i
            memo[j:n:i] = [True] * ((n - 1) // j)
        return ans
