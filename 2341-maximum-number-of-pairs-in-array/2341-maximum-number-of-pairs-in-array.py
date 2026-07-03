class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count=Counter(nums)

        pair=sum(freq//2 for freq in count.values())

        return [pair,len(nums)-2*pair]
        