from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1

        # divCnt[d] = numbers divisible by d
        divCnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for m in range(d, mx + 1, d):
                divCnt[d] += cnt[m]

        # exact[d] = pairs with gcd exactly d
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            c = divCnt[d]
            exact[d] = c * (c - 1) // 2
            for m in range(d * 2, mx + 1, d):
                exact[d] -= exact[m]

        prefix = []
        vals = []
        s = 0
        for g in range(1, mx + 1):
            if exact[g]:
                s += exact[g]
                prefix.append(s)
                vals.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(vals[idx])

        return ans