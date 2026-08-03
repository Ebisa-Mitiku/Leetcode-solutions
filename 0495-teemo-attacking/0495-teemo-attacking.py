class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans=0
        next=0

        for time in timeSeries:
            if time<next:
                ans=ans-(next-time)+duration
                next=time+duration
            else:
                ans+=duration
                next=time+duration
        return ans

        