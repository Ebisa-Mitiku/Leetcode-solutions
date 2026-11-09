class Solution:
    def minMoves(self, nums: List[int]) -> int:
        high=max(nums)
        ans=0
        for num in nums:
            ans+=high-num
        return ans
        