class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter=defaultdict(list)
        ans=[]

        for word in strs:
            temp="".join(sorted(word))
            counter[temp].append(word)

        for key in counter:
            ans.append(counter[key])
        return ans      


  
        
    
        