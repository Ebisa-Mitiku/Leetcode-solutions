class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums=Counter(nums)
        mini=0

        even=[]
        for key in nums:
            if key%2==0:
                if nums[key]>mini:
                    mini=nums[key]
        
        for key in nums:
            if key%2==0 and nums[key]==mini:
                even.append(key)
        
        if even:
            return min(even)
        return -1

                
        
        