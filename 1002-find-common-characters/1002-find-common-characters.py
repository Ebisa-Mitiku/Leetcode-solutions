class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        initial=words[0]
        ans=[]
        for i in range(len(words)):
            words[i]=list(words[i])

       
        
        for i in range(len(initial)):
            flag=True
            for j in range(1,len(words)):
                if initial[i] not in words[j]:
                    flag=False
                else:
                    words[j].remove(initial[i])
                
            if flag:
                ans.append(initial[i])
        return ans
     




        