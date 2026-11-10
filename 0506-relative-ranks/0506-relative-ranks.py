class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        final=sorted(score,reverse=True)
        rank,reward=1,{}

        for num in final:
            if rank<=3:
                if rank==1:
                    reward[num]="Gold Medal"
                elif rank==2:
                    reward[num]="Silver Medal"
                else:
                    reward[num]="Bronze Medal"
            else:
                reward[num]=str(rank)
            rank+=1

        return [reward[player] for player in score]
    
        
        