class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        ans=sorted(intervals, key=lambda x: -x[0])
        count=0
        print(ans)

        for i in range(len(ans)-1):
            for j in range(i+1,len(ans)):
                if ans[i][0]>=ans[j][0] and ans[i][1]<=ans[j][1]:
                    count+=1
                    break
        return len(ans)-count

        

       



        