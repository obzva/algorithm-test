# My solution, iteration with state machine

# Time complexity: O(N), for every char
# Space complexity: O(N), for stacks

class Solution:
    def decodeString(self, s: str) -> str:
        new_number = True
        nums = []
        chars = []
        answer = ""

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                if new_number:
                    nums.append(int(char))
                    new_number = False
                else:
                    nums[-1] = nums[-1] * 10 + int(char)

            elif char == "[":
                new_number = True
                chars.append("")

            elif char == "]":
                acc_char = chars.pop()
                repeat = nums.pop()
                if chars:
                    chars[-1] = chars[-1] + (acc_char * repeat)
                else:
                    answer += acc_char * repeat

            else:
                if chars:
                    chars[-1] = chars[-1] + char
                else:
                    answer += char

        return answer
