class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=str(nums[i])
            k=0
            for j in range(len(x)):
                k+=int(x[j])
            nums[i]=k
        return min(nums)