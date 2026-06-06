class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left=0
        rigt=0
        leftsum=[0]
        rightsum=[]
        sumnum=sum(nums)
        ans=[]

        for i in range(1,len(nums)):
            left+=nums[i-1]
            leftsum.append(left)

        for i in range(len(nums)):
            sumnum-=nums[i]
            rightsum.append(sumnum)
        for i in range(len(nums)):
            ans.append(abs(leftsum[i]-rightsum[i]))
        return ans


        
       

        