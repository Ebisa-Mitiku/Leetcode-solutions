class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left=0
        right=sum(nums)
        ans=[]

        for i in range(len(nums)):
            if i==0:
                left=0
                right-=nums[i]
                ans.append(abs(left-right))
            else:
                left+=nums[i-1]
                right-=nums[i]
                ans.append(abs(left-right))
                   
        return ans


        
       

        