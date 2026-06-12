class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num=0
        n=len(s)

        i=0
        while i<n-1:
            if roman[s[i]]>=roman[s[i+1]]:
                num+=roman[s[i]]
                i+=1
            else:
                num+=roman[s[i+1]]-roman[s[i]]
                i+=2
                
        if i==n-1:
            num+=roman[s[i]]
        return(num)





        