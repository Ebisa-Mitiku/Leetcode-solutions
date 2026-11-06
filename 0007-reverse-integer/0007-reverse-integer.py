class Solution:
    def reverse(self, x: int) -> int:
        MAX=2**31-1
        MIN=-2**31
        st=list(str(x))
        neg=False


        if st[0]=="-":
            st=list(reversed(st[1:]))
            neg=True
        else:
            st=list(reversed(st))
        

        x=(int("".join(st)))
        if neg:
            x*=-1
        
        if x>MAX or x<MIN:
            return 0
        return x