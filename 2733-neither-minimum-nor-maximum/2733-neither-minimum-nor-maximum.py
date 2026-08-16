class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if len(nums)<3:
            return -1
        return nums[-2]
        