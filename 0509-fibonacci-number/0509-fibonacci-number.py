class Solution:
    def fib(self, n: int) -> int:

        def fibonacci(x):
            if x==0 or x==1:
                return x
            
            return fibonacci(x-1)+fibonacci(x-2)
        
        return fibonacci(n)



        