class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        ans=count.most_common()
        final = [word for word, _ in sorted(ans, key=lambda x: (-x[1],x[0]))]


        return final[:k]


        