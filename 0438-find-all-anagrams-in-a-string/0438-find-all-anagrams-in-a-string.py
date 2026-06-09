class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        n=len(s)
        target=Counter(p)
        tempdict=Counter(s[0:k])
        ans=[]

        if(tempdict==target):
            ans.append(0)
        for i in range(1,n-k+1):
            tempdict[s[i-1]]-=1
            if(tempdict[s[i-1]]==0):
                del tempdict[s[i-1]]
            
            right=i+k-1
            tempdict[s[right]]=tempdict.get(s[right],0)+1

            if(tempdict==target):
                ans.append(i)
           
        return(ans)
            

       