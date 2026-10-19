class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans=[]
        for ind in range(len(nums)):
            if nums[ind]==target:
                ans.append(ind)
        return ans
        