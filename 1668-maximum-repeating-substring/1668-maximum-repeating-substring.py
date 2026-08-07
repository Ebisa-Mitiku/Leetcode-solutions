class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        substring=word
        k=0

        while True:
            if substring in sequence:
                k+=1
                substring+=word
            else:
                break
        return k
        