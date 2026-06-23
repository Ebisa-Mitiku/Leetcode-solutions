class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=set(word)
        ans=0
        for i in count:
            if i.islower() and i.upper() in count:
                ans+=1

        return ans
        