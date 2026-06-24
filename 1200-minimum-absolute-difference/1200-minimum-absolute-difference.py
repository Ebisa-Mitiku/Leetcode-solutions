class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        lst=[]
        dif=float("inf")
        for i in range(1,len(arr)):
            dif=min(dif,arr[i]-arr[i-1])
        
        
        for i in range(1,len(arr)):

            if arr[i]-arr[i-1]==dif:
                lst.append([arr[i-1],arr[i]])

        return lst
        