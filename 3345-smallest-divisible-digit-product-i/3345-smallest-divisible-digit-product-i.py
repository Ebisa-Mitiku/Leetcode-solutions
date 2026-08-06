class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            bro=list(str(n))
            ans=1
            for num in bro:
                ans*=int(num)
            if ans%t==0:
                return n
            n+=1
            