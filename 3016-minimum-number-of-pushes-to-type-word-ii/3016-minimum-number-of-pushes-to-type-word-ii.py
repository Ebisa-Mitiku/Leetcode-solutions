class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt=Counter(word)
        distnict=[i for i,j in cnt.most_common()]
        cost=1
        ans=0

        for ind,ch in enumerate(distnict):
      
            ans+=cost*cnt[ch]
            if (ind+1)%8==0:
                cost+=1
        return ans

        
        