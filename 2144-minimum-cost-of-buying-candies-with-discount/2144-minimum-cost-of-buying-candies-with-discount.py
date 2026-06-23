class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        sell=0

        for i,num in enumerate(cost):
            if i%3!=2:
                sell+=num
                
        return sell
     
      


        