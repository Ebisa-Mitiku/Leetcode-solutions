class Solution:
    def greatestLetter(self, s: str) -> str:
        word=set(s)
        ans=""

        for ch in word:
            if ch.isupper() and ch.lower() in word:
                ans=max(ans,ch)
        return ans