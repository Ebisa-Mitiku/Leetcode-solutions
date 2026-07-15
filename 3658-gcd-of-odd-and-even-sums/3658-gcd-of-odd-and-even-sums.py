class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven,sumOdd=0,0

        for i in range(1,(n*2)+1):
            if i%2:
                sumOdd+=i
            else:
                sumEven+=i
        return(gcd(sumOdd,sumEven))
