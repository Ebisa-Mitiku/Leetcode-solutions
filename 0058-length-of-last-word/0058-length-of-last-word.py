class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst=list(s)
        n=len(s)
        count=0

        for i in range(n-1,0,-1):
            if lst[i]!=" ":
                break
            else:
                del lst[i]
        n=len(lst)
        for i in range(n-1,-1,-1):
            if lst[i]==" ":
                break
            else:
                count+=1
        return count
        




        