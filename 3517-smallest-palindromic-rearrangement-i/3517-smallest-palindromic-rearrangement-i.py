class Solution:
    def smallestPalindrome(self, s: str) -> str:
        t=Counter(s)
        left=""
        mid=''
        
        for c in sorted(t):
            left+=c*(t[c]//2)
            if t[c]%2:
                mid=c
        return left+mid+left[::-1]

        

        