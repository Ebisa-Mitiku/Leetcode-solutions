class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
       
        s=sorted(s)
        t=sorted(t)

        for i in range(len(t)-1):
            if  t[i]!=s[i]:
                return t[i]
        return t[-1]
          



        