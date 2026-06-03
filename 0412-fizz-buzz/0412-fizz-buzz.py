class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[i for i in range(1,n+1)]
        b=[]
        for i in a:
            if i%3==0 and i%5==0:
                b.append("FizzBuzz")
            elif i%3==0:
                b.append("Fizz")
            elif i%5==0:
                b.append("Buzz")
            else:
                b.append(str(i))
        return b
        