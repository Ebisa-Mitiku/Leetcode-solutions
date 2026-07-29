class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt=Counter(nums)
    
        if len(set(cnt.values()))==1:
            return [-1,-1]
        
        else:
            x=min(cnt.keys())
            val=cnt[x]
            for key in sorted(cnt):
                if cnt[key]!=val:
                    y=key
                    break
            return [x,y]