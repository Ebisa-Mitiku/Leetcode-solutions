class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ran=Counter(ransomNote)
        mag=Counter(magazine)
        flag=True

        for key in ran:
            if ran[key]>mag[key]:
                flag=False
        return flag