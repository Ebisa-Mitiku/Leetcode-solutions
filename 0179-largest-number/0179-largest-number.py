class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        

        for i in range(len(nums)-1):
            for j in range(1,len(nums)-i):
                if nums[j-1]+nums[j]<nums[j]+nums[j-1]:
                    nums[j-1],nums[j]=nums[j],nums[j-1]
        result= "".join(nums)
        if result[0]=="0":
            return "0"
        return result

                

        

       
        
        