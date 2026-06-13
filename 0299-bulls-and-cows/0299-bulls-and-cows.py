class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        sc=Counter(secret)
        gu=Counter(guess)
        none=0
        for key in sc:
            if sc[key]>gu[key]:
                none+=sc[key]-gu[key]
        

        bull=0
        cow=0

        for i in range(len(guess)):
            if secret[i]==guess[i]:
                bull+=1

        cow=len(guess)-none-bull
        ans=str(bull)+"A"+str(cow)+"B"
        return ans