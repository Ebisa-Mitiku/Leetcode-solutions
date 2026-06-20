class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        ans=0
        pre=0
        for i in range(len(gain)):
            ans=max(ans,gain[i]+pre)
            pre+=gain[i]
            print(pre)
        return ans



        
        