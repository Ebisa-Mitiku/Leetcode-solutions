class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x="".join(d for d in str(n) if d!="0")

        if not x:
            return 0

        return(int(x)*sum(map(int,x)))
        