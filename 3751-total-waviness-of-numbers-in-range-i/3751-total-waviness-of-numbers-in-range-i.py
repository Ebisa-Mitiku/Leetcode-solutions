class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count=0

        if num1<100 and num2<100:
            return 0
        
        elif num1<100 and num2>=100:
            for i in range(100,num2+1):
                num=str(i)
                for j in range(1,len(num)-1):
                    if num[j-1]>num[j]<num[j+1]:
                        count+=1
                    elif num[j-1]<num[j]>num[j+1]:
                        count+=1
            return count
        else:
            for i in range(num1,num2+1):
                num=str(i)
                for j in range(1,len(num)-1):
                    if num[j-1]>num[j]<num[j+1]:
                        count+=1
                    elif num[j-1]<num[j]>num[j+1]:
                        count+=1
            return count


        