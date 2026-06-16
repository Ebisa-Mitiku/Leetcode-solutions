class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high%2==0 and low%2==0:
            return (high-low)//2
        if high%2==1 and low%2==1:
            return (high-low-1)//2+2
        else:
           return (high-low)//2+1
        