class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        cnt=Counter(nums)
        n=len(nums)

        if k==n:
            return max(nums)
        elif 1<k<n:
            if cnt[nums[0]]==1 and cnt[nums[n-1]]==1:
                return max(nums[0],nums[n-1])
            elif cnt[nums[0]]==1:
                return nums[0]
            elif cnt[nums[n-1]]==1:
                return nums[n-1]
            else:
                return -1
        else:
            largest=None
            for x in nums:
                if cnt[x]==1:
                    if largest is None or x>largest:
                        largest=x
            if largest==None:
                return -1
            return largest


            