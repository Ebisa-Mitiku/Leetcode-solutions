class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        ans=[0]

        for alt in range(len(gain)):
            ans.append(ans[-1]+gain[alt])
        return max(ans)



        
        