class Solution:
    def calculate(self, s: str) -> int:
        # MY SOLUTION
        # nums = []
        # operators = []
        # prev = 0
        # for i in range(len(s)):
        #     if s[i] in ['+', '-', '*', '/']:
        #         operators.append(s[i])
        #         nums.append(int(s[prev:i]))
        #         prev = i + 1
        #     elif i == len(s) - 1:
        #         nums.append(int(s[prev:i + 1]))
        #         prev = i + 1
        #
        # i = 0
        # plus_minus = []
        # for j in range(len(operators)):
        #     if operators[j] == '*':
        #         nums = nums[:i] + [nums[i] * nums[i + 1]] + nums[i + 2:]
        #     elif operators[j] == '/':
        #         nums = nums[:i] + [nums[i] // nums[i + 1]] + nums[i + 2:]
        #     else:
        #         plus_minus.append(operators[j])
        #         i += 1
        #
        # i = 1
        # answer = nums[0]
        # for j in range(len(plus_minus)):
        #     if plus_minus[j] == '+':
        #         answer += nums[i]
        #     else:
        #         answer -= nums[i]
        #     i += 1
        # return answer

        # MORE CLEAR ONE WITH STACK
        stack, num, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = s[i]
        return sum(stack)
