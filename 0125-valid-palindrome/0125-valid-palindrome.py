class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ans=""

        for i in s:
            if i.isalnum():
                ans+=i
        
        return ans.lower()==ans.lower()[::-1]


        