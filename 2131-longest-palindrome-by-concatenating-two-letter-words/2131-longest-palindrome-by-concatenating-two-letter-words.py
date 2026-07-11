from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        ans = 0
        center = False
        seen = set()

        for word in count:
            rev = word[::-1]

            if word == rev:              # aa, bb, cc...
                pairs = count[word] // 2
                ans += pairs * 4

                if count[word] % 2 == 1:
                    center = True

            else:
                if word not in seen:
                    ans += min(count[word], count[rev]) * 4
                    seen.add(word)
                    seen.add(rev)

        if center:
            ans += 2

        return ans