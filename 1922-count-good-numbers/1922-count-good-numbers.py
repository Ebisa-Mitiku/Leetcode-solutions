class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_count=(n+1)//2
        odd_count=(n//2)
        mod=10**9+7

        even=pow(5,even_count,mod)
        odd=pow(4,odd_count,mod)

        return even*odd%mod
        