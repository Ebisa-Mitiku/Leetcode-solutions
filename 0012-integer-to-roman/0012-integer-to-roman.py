class Solution:
    def intToRoman(self, num: int) -> str:
        # value -> symbol mapping from largest to smallest
        vals = [1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"]

        res = []
        for v, s in zip(vals, syms):
            if num == 0:
                break
            count = num // v
            if count:
                # append symbol count times (works for single- and two-letter symbols)
                res.append(s * count)
                num -= v * count
        return "".join(res)


