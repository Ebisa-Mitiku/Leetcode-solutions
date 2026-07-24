class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]

        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
            ans.append(list(reversed(image[i])))
        return ans
        