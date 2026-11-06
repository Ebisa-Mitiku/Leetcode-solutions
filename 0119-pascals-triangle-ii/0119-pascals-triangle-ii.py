class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        def pascal(n):
            if n==0:
                return [1]
        
            prev=pascal(n-1)
            current=[1]
            for i in range(len(prev)-1):
                current.append(prev[i]+prev[i+1])
            
            return current+[1]
            
        return pascal(rowIndex)

            
        