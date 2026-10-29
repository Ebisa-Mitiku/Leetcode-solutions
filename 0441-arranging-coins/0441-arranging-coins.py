class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans=(-1+sqrt(1+8*n))//2
        return int(ans)
        