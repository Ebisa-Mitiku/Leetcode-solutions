class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        left=0
        right=1
        ans=[words[0]]

        while right<len(words):
            if sorted(words[left])==sorted(words[right]):
                right+=1
            else:
                ans.append(words[right])
                left=right
                right+=1

        return ans



            



        