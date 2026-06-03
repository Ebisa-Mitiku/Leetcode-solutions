class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        n=max(nums)
        count=0
        for i in range(len(nums)):
            if nums[i] in seen:
                nums[i]=n+1
                count+=1
            else:
                seen.add(nums[i])
        nums.sort()
        return len(nums)-count
        
        

        

        