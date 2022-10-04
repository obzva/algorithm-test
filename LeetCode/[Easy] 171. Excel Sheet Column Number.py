class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # MY SOLUTION
        #
        # dic = {}
        # for i in range(26):
        #     dic[chr(i + 65)] = i + 1
        #
        # nums = []
        # for col in columnTitle:
        #     nums.append(dic[col])
        # nums = nums[::-1]
        #
        # answer = 0
        # for i, num in enumerate(nums):
        #     answer += num * 26 ** i
        #
        # return answer

        # MY SOLUTION OPTIMIZATION

        answer = 0
        for column in columnTitle:
            answer = answer * 26 + ord(column) - 64
        return answer
