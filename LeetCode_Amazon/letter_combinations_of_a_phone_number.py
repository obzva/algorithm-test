class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        if digits == "":
            return output
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def rec(prev: str, remain: str):
            if len(remain) == 0:
                output.append(prev)
                return
            first_digit = remain[0]
            for letter in hashmap[first_digit]:
                rec(prev + letter, remain[1:])

        rec("", digits)
        return output
