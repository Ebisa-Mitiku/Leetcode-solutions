class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return prod(nums)

        nums.sort()
        neg=0

        for i in range(len(nums)):
            if nums[i]<0:
                neg+=1

        if neg<2:
            return nums[-1]*nums[-2]*nums[-3]

        x=nums[-1]*nums[-2]*nums[-3]
        y=nums[0]*nums[1]*nums[-1]
        return max(x,y)

        

     