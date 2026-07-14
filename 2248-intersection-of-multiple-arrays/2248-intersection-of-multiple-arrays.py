class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        count={}
        for num in nums:
            for x in num:
                count[x]=count.get(x,0)+1

        return sorted([num for num in count if count[num]==len(nums)])
        