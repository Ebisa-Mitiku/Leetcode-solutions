class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twn=0

        for bill in bills:
            if bill==20:
                twn+=1
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False 
            elif bill==10:
                ten+=1
                if five>=1:
                    five-=1
                else:
                    return False   
            else:
                five+=1
        return True




        