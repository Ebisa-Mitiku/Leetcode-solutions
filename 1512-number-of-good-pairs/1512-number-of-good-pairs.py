class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for key in count:
            ans+=(count[key]*(count[key]-1))//2
        return ans
        