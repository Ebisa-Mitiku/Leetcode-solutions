class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        def isDivided(x):
            if x==1:
                return True

            if x<1 or x%4!=0:
                return False
            return isDivided(x/4)

        return isDivided(n)
        