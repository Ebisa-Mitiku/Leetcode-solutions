class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        final=sorted(score,reverse=True)
        reward={}
        medals=["Gold Medal","Silver Medal", "Bronze Medal"]
        for rank,num in enumerate(final,1):
            reward[num]=medals[rank-1] if rank<=3 else str(rank)

        return [reward[player] for player in score]
    
        
        