class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr=Counter(arr)
        luck=[]

        for key in arr:
            if arr[key]==key:
                luck.append(key)    
        if luck:
            return max(luck)
        return -1  