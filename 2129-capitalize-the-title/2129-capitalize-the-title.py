class Solution:
    def capitalizeTitle(self, title: str) -> str:

        string=title.split()
        for i in range(len(string)):
            if len(string[i])<=2:
                string[i]=string[i].lower()
            else:
                string[i]=string[i][0].upper()+string[i][1:].lower()
        return " ".join(string)
                
        