class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)

        odd=0
        ans=0
        for x in count.values():
            if x%2:
                odd+=1
                ans+=x-1
            else:
                ans+=x
        if odd:
            ans+=1
        return ans

        
        