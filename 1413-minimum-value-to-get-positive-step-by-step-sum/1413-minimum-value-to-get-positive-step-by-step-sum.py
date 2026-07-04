class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start=0
        l=[]

        for i in range(len(nums)):
            start+=nums[i]
            l.append(start)
        
        if min(l)<0:
            return -1*(min(l))+1
        return 1

        