class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        n=len(nums)

        for i in range(n-2):
            for j in range(i,n-1):
                for k in range(j,n):
                    if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                        count+=1
        return count
        