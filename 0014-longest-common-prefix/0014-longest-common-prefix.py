class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f=True
        strs.sort(key=len)
        x=""
        fl=strs[0]

        for i in range(len(fl)):
            for j in range(1,len(strs)):
                if fl[i]!=strs[j][i]:
                    f=False
                    break
            if  f:
                x+=fl[i]
        return x

                    
        

        