class Solution:
    def toLowerCase(self, s: str) -> str:
        word=list(s)
        for i in range(len(word)):
            if word[i].isupper():
                word[i]=word[i].lower()
        return "".join(word)
        