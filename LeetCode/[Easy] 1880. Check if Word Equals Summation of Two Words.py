class Solution:
    def to_number(self, char: str) -> int:
        return ord(char) - 97

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_value, second_value, target_value = 0, 0, 0
        for char in firstWord:
            first_value = first_value * 10 + self.to_number(char)
        for char in secondWord:
            second_value = second_value * 10 + self.to_number(char)
        for char in targetWord:
            target_value = target_value * 10 + self.to_number(char)
        return first_value + second_value == target_value
