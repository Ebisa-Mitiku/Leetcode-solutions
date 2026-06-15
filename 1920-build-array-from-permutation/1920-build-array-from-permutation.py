class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        ans=[]
        for i in range(len(nums)):
            x=nums[i]
            ans.append(nums[x])
        return ans
        