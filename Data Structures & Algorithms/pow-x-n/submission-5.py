class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Divide and conquer with O(1) space
        def calculate(x:int, n: int):
            if x == 0:
                return 0
            if n == 0:
                return 1

            odd_n = n % 2
            n = n - 1 if odd_n else n

            half = calculate(x, n//2)
            multiplier = x if odd_n else 1
            return half * half * multiplier
        
        res = calculate(x, abs(n))
        return 1/res if n < 0 else res