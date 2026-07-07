class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=""

        for num in str(n):
            if num!="0":
                x+=num
                
        if not x:
            return 0

        ans=0
        for i in x:
            ans+=int(i)


        return(int(x)*ans)
        