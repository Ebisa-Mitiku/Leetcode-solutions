class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        n=len(s2)
        target=Counter(s1)
        tempdict=Counter(s2[0:k])
   

        if tempdict==target:
            return True
        for i in range(1,n-k+1):
            tempdict[s2[i-1]]-=1

            if tempdict[s2[i-1]]==0:
                del tempdict[s2[i-1]]
            
            right=i+k-1
            tempdict[s2[right]]=tempdict.get(s2[right],0)+1

            if tempdict==target:
                return True
           
        return False
            
        