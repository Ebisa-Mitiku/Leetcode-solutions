class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
       
        s={"b","a","l","o","n"}
        dic={}
        for i in range(len(text)):
            if text[i] in s:
                dic[text[i]]=dic.get(text[i],0)+1


        if len(set(dic))<5:
            return 0
        limiter=float("inf")
        for key in dic:
            if key in s:
                if key=="o" or key=="l":
                    limiter=min(limiter,dic[key]//2)
                else:
                    limiter=min(limiter,dic[key])
        return limiter

        


        