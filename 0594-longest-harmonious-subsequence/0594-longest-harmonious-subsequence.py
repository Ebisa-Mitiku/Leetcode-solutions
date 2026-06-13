class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count=Counter(nums)
        maxi=0

        for key in count:
            if key+1 in count:
                maxi=max(maxi,count[key]+count[key+1])

        return maxi

  
        