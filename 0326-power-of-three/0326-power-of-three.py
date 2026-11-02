class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def isDivided(x):
            if x==1:
                return True
            
            if x<1 or x%3!=0:
                return False
            return isDivided(x/3)
        return isDivided(n)
        