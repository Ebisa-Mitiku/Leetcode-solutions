class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for ch in operations:
            if ch=="+":
                ans.append(ans[-1]+ans[-2])
            elif ch=="C":
                ans.pop()
            elif ch=="D":
                ans.append(ans[-1]*2)
            else:
                ans.append(int(ch))
                
        return sum(ans)
        