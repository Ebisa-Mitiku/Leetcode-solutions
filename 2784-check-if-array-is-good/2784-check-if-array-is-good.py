class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        return(
            len(nums)==m+1 and len(set(nums))==m and nums.count(m)==2
        )