class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiop"
        b="asdfghjkl"
        c="zxcvbnm"
        ans=[]
        
        for word in words:
            temp=word.lower()
            where=set()
            for ch in temp:
                if ch in a:
                    where.add("a")
                elif ch in b:
                    where.add("b")
                else:
                    where.add("c")
            if len(where)==1:
                ans.append(word)
        return ans
            
                