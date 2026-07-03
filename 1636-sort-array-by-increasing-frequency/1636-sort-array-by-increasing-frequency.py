class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)

        return [
            num
            for num in sorted(nums,key=lambda x:(freq[x],-x))
        ]
        