class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        x="abcdefghijklmnopqrstuvwxyz"
        letter={}
        for i,j in enumerate(x):
            letter[j]=i

        ans=""
        

        for word in words:
            sum=0
            for j in range(len(word)):
                sum+=weights[letter[word[j]]]

            sum%=26
            sum=25-sum
            for key in letter:
                if letter[key]==sum:
                    ans+=key
                    break

        return(ans)



        