class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}

        res = n
        while res != 1:
            temp = res
            res = 0
            while True:
                res += (temp % 10)**2
                if temp % 10 == temp:
                    break
                temp //= 10
            if res in seen:
                return False
            seen.add(res)
        
        return True


        