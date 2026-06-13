class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        ans=[]


        for i in range(n):
            if nums[i]==1:
                count+=1
            else:
                ans.append(count)
                count=0

        ans.append(count)
        return(max(ans))


            


            
            
        