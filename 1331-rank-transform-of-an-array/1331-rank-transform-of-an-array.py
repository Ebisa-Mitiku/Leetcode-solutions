class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        count=sorted(arr)
        dic={}
        i=1

        for x in count:
            if x not in dic:
                dic[x]=i
                i+=1
                
        return [dic[num] for num in arr ]
