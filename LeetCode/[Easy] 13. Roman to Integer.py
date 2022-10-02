class Solution:
    def romanToInt(self, s: str) -> int:
        # answer = 0
        # for i in range(len(s)):
        #     if s[i] == 'M':
        #         answer += 1000
        #     if s[i] == 'D':
        #         answer += 500
        #     if s[i] == 'C':
        #         if i < len(s) - 1 and (s[i + 1] == 'D' or s[i + 1] == 'M'):
        #             answer -= 100
        #         else:
        #             answer += 100
        #     if s[i] == 'L':
        #         answer += 50
        #     if s[i] == 'X':
        #         if i < len(s) - 1 and (s[i + 1] == 'L' or s[i + 1] == 'C'):
        #             answer -= 10
        #         else:
        #             answer += 10
        #     if s[i] == 'V':
        #         answer += 5
        #     if s[i] == 'I':
        #         if i < len(s) - 1 and (s[i + 1] == 'V' or s[i + 1] == 'X'):
        #             answer -= 1
        #         else:
        #             answer += 1
        #
        # return answer
        answer = 0
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD',
                                                                                                                'CCCC').replace(
            'CM', 'DCCCC')
        for roman in s:
            answer += dic[roman]
        return answer
