class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter=defaultdict(list)
        for word in strs:
            temp="".join(sorted(word))
            counter[temp].append(word)
        return(list(counter.values()))



  
        
    
        