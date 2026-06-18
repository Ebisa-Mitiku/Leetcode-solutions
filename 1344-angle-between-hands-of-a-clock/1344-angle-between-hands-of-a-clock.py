class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_deg=6*minutes

        hour_deg=( 30*hour+ 0.5* minutes)%360

        ans=abs(hour_deg-min_deg)
        
        return (min(360-ans,ans))
