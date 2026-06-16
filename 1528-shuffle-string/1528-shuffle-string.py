class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=""
        count=zip(s,indices)
        Sorted_count=sorted(count,key=lambda x:x[1])
        for key,val in Sorted_count:
            ans+=key
        return ans

        

        