class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for num in range(len(nums)):
            n=str(nums[num])
            digit=0
            for i in n:
                digit+=int(i)
            if digit==num:
                return num
        return -1
        