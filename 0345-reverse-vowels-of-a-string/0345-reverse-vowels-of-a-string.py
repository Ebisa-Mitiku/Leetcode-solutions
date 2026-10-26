class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={"a","e","i","o","u","A","E","I","O","U"}
        ori=list(s)
        left=0
        right=len(s)-1

        while left<right:
            if ori[left] in vowels and ori[right]  in vowels:
                ori[left],ori[right]=ori[right],ori[left]
                left+=1
                right-=1
            elif ori[left] in vowels and ori[right] not in vowels:
                right-=1
                
            elif ori[left] not in vowels and ori[right]  in vowels:
    
                left+=1 
            else:
                left+=1
                right-=1
        return ''.join(ori)
                
            