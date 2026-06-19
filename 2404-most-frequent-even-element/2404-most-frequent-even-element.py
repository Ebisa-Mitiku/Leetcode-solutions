class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums=Counter(nums)
        mini=0
        ans=-1

        for key in nums:
            if key%2==0:
                if nums[key]>mini:
                    mini=nums[key]
                    ans=key
                elif nums[key]==mini and key<ans:
                    ans=key
        
        return ans


                
        
        