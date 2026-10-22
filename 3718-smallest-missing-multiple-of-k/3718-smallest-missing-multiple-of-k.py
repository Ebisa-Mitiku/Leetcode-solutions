class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        current_prod=1
        nums=set(nums)
        
        while k*current_prod in nums:
            current_prod+=1
    
        return k*current_prod

