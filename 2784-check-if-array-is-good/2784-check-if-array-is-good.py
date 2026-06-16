class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        nm=nums.count(m)

        if len(nums)!=m+1:
            return False
        
        elif len(set(nums))!=m:
            return False
        elif nm==2:
            return True

        return False
     