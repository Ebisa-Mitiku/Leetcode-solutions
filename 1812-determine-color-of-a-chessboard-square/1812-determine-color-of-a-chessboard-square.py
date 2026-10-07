class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        hash={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        
        if (hash[coordinates[0]])%2 != int(coordinates[1])%2:
            return True
        return False


        