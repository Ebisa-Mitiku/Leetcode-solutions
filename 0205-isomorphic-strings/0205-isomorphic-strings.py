class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dic={}
        dit={}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=t[i]
            else:
                if dic[s[i]]!=t[i]:
                    return False

            if t[i] not in dit:
                dit[t[i]]=s[i]
            else:
                if dit[t[i]]!=s[i]:
                    return False

        return True

             