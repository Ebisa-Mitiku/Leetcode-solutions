class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix=float("inf")
        prefix_sum=0


        for i in range(len(nums)):
            prefix_sum+=nums[i]
            min_prefix=min(min_prefix,prefix_sum)
            
        
        if min_prefix<0:
            return -1*(min_prefix)+1
        return 1

        