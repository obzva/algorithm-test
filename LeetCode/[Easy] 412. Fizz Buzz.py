from typing import *


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(n):
            j = i + 1
            if j % 15 == 0:
                answer.append('FizzBuzz')
            elif j % 3 == 0:
                answer.append('Fizz')
            elif j % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(j))
        return answer
