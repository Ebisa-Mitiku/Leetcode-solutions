class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        for ch in "!?',;.":
            paragraph=paragraph.replace(ch," ")
        count=Counter(paragraph.lower().split())
        
        for key,val in count.most_common():
            if key not in banned:
                return key
               
        
        
