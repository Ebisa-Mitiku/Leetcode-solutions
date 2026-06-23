class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        ans=float("inf")

        for i in range(len(landStartTime)):
            final=landStartTime[i]+landDuration[i]
            for j in range(len(waterDuration)):
                temp=max(final,waterStartTime[j])
                ans=min(ans,temp+waterDuration[j])

        for i in range(len(waterStartTime)):
            final=waterStartTime[i]+waterDuration[i]

            for j in range(len(landDuration)):
                temp=max(final,landStartTime[j])
                ans=min(ans,temp+landDuration[j])

        return ans

        