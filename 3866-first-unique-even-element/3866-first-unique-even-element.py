class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt=Counter(nums)
        for num in nums:
            if num%2==0 and cnt[num]==1:
                return num
        return -1
        