class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def isDivided(x):
            if x==1:
                return True
            
            if x<1 or x%2!=0:
                return False
            return isDivided(x/2)
        return isDivided(n)
        