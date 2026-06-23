class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()

        sell=sum(cost)
        i=len(cost)-3
        while i>=0:
            sell-=cost[i]
            i-=3
        print(cost)
        return sell
     
      


        