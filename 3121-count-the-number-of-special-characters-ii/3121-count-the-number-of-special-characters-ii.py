class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper={}
        lower={}
        ans=0

        for i,ch in enumerate(word):
            if ch.isupper():
                if ch not in upper:
                    upper[ch]=i
            else:
                lower[ch]=i


        for ch in lower:
            x=ch.upper()
            if x in upper and  lower[ch]<upper[x]:
                ans+=1
        return ans
                
