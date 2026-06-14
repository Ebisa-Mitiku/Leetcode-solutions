class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i]=str(digits[i])

        given=int("".join(digits))+1

        ans=list(str(given))
        for i in range(len(ans)):
            ans[i]=int(ans[i])
        return ans

