class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in nums:
            return [-1,-1]
     
        l=0
        r=len(nums)-1
        ans=[]

        while l<len(nums):
            if nums[l]==target:
                    ans.append(l)
                    break
            l+=1
      
        while r>-1:
            if nums[r]==target:
                    ans.append(r)
                    break
            r-=1
        return(ans)

        
                
            




        