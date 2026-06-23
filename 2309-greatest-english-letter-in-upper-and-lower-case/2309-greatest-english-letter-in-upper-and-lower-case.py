class Solution:
    def greatestLetter(self, s: str) -> str:
        word=set(s)
        ans=[]

        for ch in word:
            if ch.islower():
                uc=ch.upper()
                if uc in word:
                    ans.append(uc)

        if ans:
            return max(ans)
        return ""
        