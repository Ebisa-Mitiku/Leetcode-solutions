from collections import defaultdict, Counter
from bisect import bisect_right
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)

        for i, ch in enumerate(s):
            pos[ch].append(i)

        freq = Counter(words)
        ans = 0

        for word, cnt in freq.items():
            last = -1

            for ch in word:
                if ch not in pos:
                    break

                idx = bisect_right(pos[ch], last)
                if idx == len(pos[ch]):
                    break

                last = pos[ch][idx]
            else:
                ans += cnt

        return ans