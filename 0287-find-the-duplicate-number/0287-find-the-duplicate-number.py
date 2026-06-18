class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count=Counter(nums)
        for i in count:
            if count[i]>=2:
                return i
        