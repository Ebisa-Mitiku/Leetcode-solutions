class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=[0]*len(nums)
        mxi=0

        for i in range(len(nums)):
            if nums[i]>mxi:
                mxi=nums[i]
            prefixGcd[i]=(gcd(mxi,nums[i]))

        prefixGcd.sort()
        
        r,l,ans=len(nums)-1,0,0
    

        while l<r:
            ans+=gcd(prefixGcd[l],prefixGcd[r])
            r-=1
            l+=1

        return(ans)
        