class Solution:
    def climbStairs(self, n: int) -> int:
        lst=[1,1]

        for i in range(n-1):
            i+=2
            lst.append(lst[i-1]+lst[i-2])

        return(lst[-1])

        
        