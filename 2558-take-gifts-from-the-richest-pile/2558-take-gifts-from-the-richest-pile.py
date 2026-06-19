class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range(k):
            x=max(gifts)
            for j in range(len(gifts)):
                if gifts[j]==x:
                    gifts[j]=int(gifts[j]**0.5)
                    break
                   

        return(sum(gifts))


        