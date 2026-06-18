class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        given=current.split(":")
        convert=correct.split(":")
        min1=int(given[0])*60+int(given[1])
        min2=int(convert[0])*60+int(convert[1])

        dif=min2-min1


        count=0
        while dif!=0:
            if dif>=60:
                dif-=60
                count+=1
            elif dif>=15:
                dif-=15
                count+=1
            elif dif>=5:
                dif-=5
                count+=1
            else:
                dif-=1
                count+=1
        return count
        