class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 1 or x == 0:
            return x
        if x == -1:
            return x if n % 2 else -1 * x
     
        negative_n = n < 0
        n = -1 * n if negative_n else n
        odd_n = n % 2
        n = n - 1 if odd_n else n
        
        candidates = [(1, 0), (x, 1)]
        while candidates[-1][1] < n:
            new_num = candidates[-1][0] * candidates[-1][0]
            new_power = candidates[-1][1] * 2
            candidates.append((new_num, new_power))
        
        res = 1
        res_power = 0
        i = len(candidates) - 1
        while res_power != n:
            while res_power + candidates[i][1] > n:
                i -= 1
            res *= candidates[i][0]
            res_power += candidates[i][1]
        
        if odd_n:
            res *= x
        
        return 1/res if negative_n else res