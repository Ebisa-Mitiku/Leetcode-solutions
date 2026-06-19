class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        count=0
        for money in accounts:
            count=max(count,sum(money))
        return count
        