class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count=Counter(s)

        limit=float('inf')

        for ch in target:
            limit=min(limit,count[ch]//target.count(ch))
        return limit       