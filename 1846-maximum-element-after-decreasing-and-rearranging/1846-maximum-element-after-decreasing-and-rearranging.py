class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        l=0
        count=1
      
    
        while l<len(arr):
            if arr[l]>=count:
                count+=1
            l+=1

         
        print(arr)
        return count-1



    
        


        