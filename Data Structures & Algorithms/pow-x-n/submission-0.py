class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n 
        def pow_(x,n):

            if n==0:
                return 1
            half = pow_(x,n//2)
            if n%2==0:
                return half*half 
            else:
                return x*half*half
        return pow_(x,n)
