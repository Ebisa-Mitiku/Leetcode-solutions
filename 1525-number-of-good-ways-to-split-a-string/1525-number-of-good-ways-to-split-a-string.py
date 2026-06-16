class Solution:
    def numSplits(self, s: str) -> int:
        ans=0
        count=Counter(s)

        dic={}

        for i in s:
            dic[i]=dic.get(i,0)+1
            count[i]-=1
            if count[i]==0:
                del count[i]
            if len(count)==len(dic):
                ans+=1
  
        return ans
