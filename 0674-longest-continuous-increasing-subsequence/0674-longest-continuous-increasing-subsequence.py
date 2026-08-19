class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        current_length=1
        longest=1
        left=0
        right=1
       

        while right<len(nums):
            if nums[right]>nums[left]:
                current_length+=1 
            else:
                longest=max(longest,current_length)
                current_length=1
            left+=1
            right+=1
        longest=max(longest,current_length)  
        return longest


            
        