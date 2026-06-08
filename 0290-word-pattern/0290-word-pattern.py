class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool: 
       
        s=s.split()
        if len(s)!=len(pattern):
            return False

        ans={}
        for i in range(len(s)):
            if s[i] in ans:
                if ans[s[i]]!=pattern[i]:
                    return False
            elif pattern[i] in ans.values():
                return False
            else:
                ans[s[i]]=pattern[i]
            
               
        return True


     
      
        

        




   

        
     
        