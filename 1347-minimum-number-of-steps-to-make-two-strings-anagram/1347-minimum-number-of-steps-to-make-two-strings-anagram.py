class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s=Counter(s)
        t=Counter(t)

        min_step=0
        for key in s:
            if s[key]>=t[key]:
                min_step+=(s[key]-t[key])

        return(min_step)

        
        
        