class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for account in accounts:
            result = max(result, sum(account))
        return result
