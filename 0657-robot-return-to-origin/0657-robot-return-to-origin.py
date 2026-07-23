class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up=moves.count("U")
        down=moves.count("D")
        right=moves.count("R")
        left=moves.count("L")

        return right-left==0 and up-down==0
        