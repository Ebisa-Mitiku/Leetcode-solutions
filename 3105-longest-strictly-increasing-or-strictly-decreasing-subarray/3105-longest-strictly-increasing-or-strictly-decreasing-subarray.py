class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=1
        ansinc=1
        dec=1
        ansdec=1
        
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                inc+=1
            else:
                ansinc=max(inc,ansinc)
                inc=1
            
            if nums[i+1]<nums[i]:
                dec+=1
            else:
                ansdec=max(dec,ansdec)
                dec=1
        ansinc=max(inc,ansinc) 
        ansdec=max(dec,ansdec)    
        return max(ansinc,ansdec)

            
        


        