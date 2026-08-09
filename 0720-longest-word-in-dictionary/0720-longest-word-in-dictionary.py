class Solution:
    def longestWord(self, words: List[str]) -> str:
        s=set(words)
        ans=[]
        m=0
        

        for word in words:
            flag=True
            if len(word)!=1:
                for i in range(len(word)-1):
                    if word[0:i+1] not in s:
                        flag=False
            if flag:
                if m<=len(word):
                    m=len(word)
                    ans.append(word)
        ans.sort()
        if len(ans)!=0:
            for word in ans:
                if len(word)==m:
                    return word
        return ""
            
        