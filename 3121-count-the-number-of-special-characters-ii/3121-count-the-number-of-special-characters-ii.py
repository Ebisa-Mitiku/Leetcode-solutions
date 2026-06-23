class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        seen_upper=set()
        seen_lower=set()
        upper={}
        lower={}
        ans=0

        for i,j in enumerate(word):
            if not j in seen_upper and j.isupper():
                seen_upper.add(j)
                upper[j]=i
                
        for i in range(len(word)-1,-1,-1):
            if not word[i] in seen_lower and word[i].islower():
                seen_lower.add(word[i])
                lower[word[i]]=i


        for ch in lower:
            x=ch.upper()
            if x in seen_upper and  lower[ch]<upper[x]:
                ans+=1
        return ans
                
