class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        final=sorted(abs(num) for num in nums)
       
        mid=len(final)//2
        
        minus=0
        plus=0

        for i in range(len(final)):
            if i<mid:
                minus+=final[i]*final[i]
             
            else:
                plus+=final[i]*final[i]
        return plus-minus
               

       


        