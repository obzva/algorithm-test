import math
from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    value = operand1 + operand2
                elif token == '-':
                    value = operand1 - operand2
                elif token == '*':
                    value = operand1 * operand2
                else:
                    value = math.trunc(operand1 / operand2)
                stack.append(value)
            else:
                stack.append(int(token))
        return stack.pop()
