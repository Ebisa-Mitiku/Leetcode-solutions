class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) == 3:
                count += len(s) - right

                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

        return count