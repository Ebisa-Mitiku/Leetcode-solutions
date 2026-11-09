class Solution:
    def minMoves(self, nums: List[int]) -> int:
        high,ans=max(nums),0
        return sum([ans+high-num for num in nums])
      