class Solution:
    def frequencySort(self, s: str) -> str:
        s=Counter(s)
        s=sorted(s.items(),key=lambda x:x[1],reverse=True)
        
        x=""
        for key,val in s:
            x+=key*val

        return x

        