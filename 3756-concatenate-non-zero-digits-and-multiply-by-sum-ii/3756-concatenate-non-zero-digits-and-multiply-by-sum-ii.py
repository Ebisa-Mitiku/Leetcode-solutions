class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        digits = []
        positions = []

        # Store non-zero digits and their positions
        for i in range(len(s)):
            if s[i] != '0':
                digits.append(int(s[i]))
                positions.append(i)

        n = len(digits)

        # Prefix sum of digits
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + digits[i]

        # Powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix concatenated numbers
        prefix_num = [0] * (n + 1)
        for i in range(n):
            prefix_num[i + 1] = (prefix_num[i] * 10 + digits[i]) % MOD

        # First index with position >= target
        def lower_bound(target):
            left = 0
            right = len(positions)

            while left < right:
                mid = (left + right) // 2
                if positions[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        # First index with position > target
        def upper_bound(target):
            left = 0
            right = len(positions)

            while left < right:
                mid = (left + right) // 2
                if positions[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        ans = []

        for l, r in queries:
            L = lower_bound(l)
            R = upper_bound(r) - 1

            if L > R:
                ans.append(0)
                continue

            digit_sum = pref_sum[R + 1] - pref_sum[L]

            length = R - L + 1

            number = (prefix_num[R + 1] -
                      prefix_num[L] * pow10[length]) % MOD

            ans.append((number * digit_sum) % MOD)

        return ans