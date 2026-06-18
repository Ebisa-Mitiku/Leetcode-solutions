class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degmin=int(30*(minutes)/5)
        totalmin=((hour*60+minutes)/60)*30
        if totalmin>360.0:
            totalmin-=360.0
        
        ans=abs(degmin-totalmin)
        return (min(360-ans,ans))
