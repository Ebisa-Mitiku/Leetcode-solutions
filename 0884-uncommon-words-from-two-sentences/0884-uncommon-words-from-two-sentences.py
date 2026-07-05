class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts1=Counter(s1.split())
        counts2=Counter(s2.split())
        ans=[]

        for word in counts1:
            if counts1[word]<2 and counts2[word]==0:
                ans.append(word)

        for word in counts2:
            if counts2[word]<2 and counts1[word]==0:
                ans.append(word)
        return ans