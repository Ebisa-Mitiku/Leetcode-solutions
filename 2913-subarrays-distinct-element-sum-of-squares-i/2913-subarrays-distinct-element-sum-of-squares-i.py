class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)

        for start in range(n):
            for end in range(start+1,n+1):
                ans+=len(set(nums[start:end]))**2
        return ans


        