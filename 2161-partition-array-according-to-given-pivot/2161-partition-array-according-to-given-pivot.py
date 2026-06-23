class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less,great,equal=[],[],[]
        for num in nums:
            if num==pivot:
                equal.append(num)
            elif num<pivot:
                less.append(num)
            else:
                great.append(num)
        return less+equal+great
        