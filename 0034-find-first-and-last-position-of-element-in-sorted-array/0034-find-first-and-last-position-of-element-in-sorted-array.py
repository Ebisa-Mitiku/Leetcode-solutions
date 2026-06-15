class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in nums:
            return [-1,-1]
        ans=[]
        
        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i)

        result=[ans[0],ans[-1]]
        return result


        