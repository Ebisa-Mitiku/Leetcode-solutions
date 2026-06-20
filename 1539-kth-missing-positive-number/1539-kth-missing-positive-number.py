class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans=[]
        for i in range(1,len(arr)+k+1):
            if i not in arr:
                ans.append(i)

        return ans[k-1]
        
        