class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count=Counter(s)
        t_count=Counter(target)

        limit=float('inf')

        for ch in target:
            limit=min(limit,count[ch]//t_count[ch])
            
        return limit       