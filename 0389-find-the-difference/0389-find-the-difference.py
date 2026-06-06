class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    
        dics={}
        dic={}
          
        for i in s:
            dics[i]=dics.get(i,0)+1
        
        for i in t:
            dic[i]=dic.get(i,0)+1
        
        for i in dic:
            if i not in dics:
                return i

            if dic[i]!=dics[i]:
                return i

       

        

           



        