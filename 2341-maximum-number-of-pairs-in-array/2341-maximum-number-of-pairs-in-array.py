class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count=Counter(nums)

        pair=0

        for key in count:
            pair+=count[key]//2

        return [pair,len(nums)-2*pair]
        