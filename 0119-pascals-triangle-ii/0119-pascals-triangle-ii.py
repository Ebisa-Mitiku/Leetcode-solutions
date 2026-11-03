class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        def pascal(n):
            if n == 0:
                return [1]

            prev = pascal(n - 1)

            row = [1]

            for i in range(1, len(prev)):
                row.append(prev[i - 1] + prev[i])

            row.append(1)

            return row

        return pascal(rowIndex)
            
        