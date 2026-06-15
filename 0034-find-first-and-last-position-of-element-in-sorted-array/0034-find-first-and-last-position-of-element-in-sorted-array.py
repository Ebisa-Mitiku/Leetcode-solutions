class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        first,last=-1,-1


        while l<=r:
            if first==-1:
                if nums[l]==target:
                    first=l    
                else:
                    l+=1
            if last==-1:
                if nums[r]==target:
                    last=r
                else:
                    r-=1
            if first!=-1 and last!=-1:
                break

        return [first,last]


        
                
            




        