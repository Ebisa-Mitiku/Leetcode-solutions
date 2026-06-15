class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short=min(strs,key=len)


        for i in range(len(short)):
            for s in strs:
                if s[i]!=short[i]:
                    return short[:i]
       
        return short

                    
        

        