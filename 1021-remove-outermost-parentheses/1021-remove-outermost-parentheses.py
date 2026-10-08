class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ans=""

        for i in range(len(s)):
            if stack.count("(")==stack.count(")") and stack:
                stack.pop(0)
                stack.pop()
                ans+="".join(stack)
                stack=[]
            stack.append(s[i])
        if stack:
            stack.pop(0)
            stack.pop()
            ans+="".join(stack)
        return ans

            
        