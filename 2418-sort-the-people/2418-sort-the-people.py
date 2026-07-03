class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        
        high=list(zip(names,heights))
    
        return [
            name
            for name,_ in sorted(high,key= lambda x:-x[1])
            ]

      