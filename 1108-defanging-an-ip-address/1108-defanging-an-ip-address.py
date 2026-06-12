class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=list(address)
        for i in range(len(s)):
            if s[i]==".":
                s[i]="[.]"
        return ''.join(s)

        