class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # sort method의 key로 lambda 함수 지정
        # 식별자를 제외한 문자열 [1:]을 키로하여 정렬하며, 동일한 경우 후순위로 식별자 [0]을 지정하여 정렬되도록 함
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits
