class Solution:
    def maxDifference(self, s: str) -> int:
        cnt=Counter(s)

        maxOdd=max([freq for freq in cnt.values() if freq%2])
        minEven=min([freq for freq in cnt.values() if freq%2==0])
        return maxOdd-minEven
            

        