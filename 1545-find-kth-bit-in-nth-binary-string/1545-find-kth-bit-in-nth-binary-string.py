class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            x=""
            for i in range(len(s)):
                if s[i]=="0":
                    x+="1"
                else:
                    x+="0"
            return x

        def Sn(x):
            if x==1:
                return "0"
            prev=Sn(x-1)
            return prev+"1"+invert(prev[::-1])

        return Sn(n)[k-1]
        