class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        transposed=zip(*matrix)
        for idx,row in enumerate(transposed):
            matrix[idx]=list(reversed(row))

      
        