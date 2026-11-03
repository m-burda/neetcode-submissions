class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        
        def sumOfSquares(n: int) -> int:
            res = 0
            while True:
                res += (n % 10)**2
                if n % 10 == n:
                    break
                n //= 10
            return res

        while n != 1:
            res = sumOfSquares(n)
            if res in seen:
                return False
            seen.add(res)
            n = res
        

        return True


        