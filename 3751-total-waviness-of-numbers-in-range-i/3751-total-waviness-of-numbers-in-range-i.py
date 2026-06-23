class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count=0
        start=max(100,num1)

        for i in range(start,num2+1):
            num=str(i)
            for j in range(1,len(num)-1):
                if num[j-1]>num[j]<num[j+1] or num[j-1]<num[j]>num[j+1]:
                    count+=1

        return count



        