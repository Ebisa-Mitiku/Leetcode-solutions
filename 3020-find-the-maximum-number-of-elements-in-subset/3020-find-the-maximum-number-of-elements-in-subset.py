class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=1

        if 1 in count:
            ans=max(ans,count[1] if count[1]%2 else count[1]-1)
        
        for x in count:
            if x==1:
                continue
            
            curr=x
            length=0

            while count[curr]>=2:
                length+=2
                curr*=curr

            if count[curr]==1:
                length+=1
            else:
                length-=1
            
            ans=max(ans,length)

        return ans

        