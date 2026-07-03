class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
   
        return[
            word 
            for word, _ in sorted(count.items(), key=lambda x: (-x[1],x[0]))][:k]


        


        