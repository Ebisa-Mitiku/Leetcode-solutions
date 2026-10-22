class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        multiplier=1
        
        while k*multiplier in nums:
            multiplier+=1
    
        return k*multiplier

