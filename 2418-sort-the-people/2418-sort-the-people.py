class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        	return [
            names[name]
            for name in sorted(range(len(names)),key= lambda x:-heights[x])
            ]

      