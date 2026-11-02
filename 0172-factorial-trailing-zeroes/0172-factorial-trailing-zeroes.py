

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        
        return n//5+self.trailingZeroes(n//5)
        # def factorial(n):
        #     if n==0:
        #         return 1
        #     return n*factorial(n-1)

        # s=factorial(n)
        # ans=0

        # while s>0:
        #     if s%10==0:
        #         ans+=1
        #         s//=10
        #     else:
        #         break
        # return ans




        