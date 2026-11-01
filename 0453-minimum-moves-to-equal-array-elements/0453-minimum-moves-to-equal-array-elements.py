class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val=min(nums)
        ans=0
        for num in nums:
            ans+=num-min_val
        return ans
        