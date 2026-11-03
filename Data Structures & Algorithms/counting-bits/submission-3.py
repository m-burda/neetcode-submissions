class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1]
        if n <= 1:
            return res[:n + 1]
        
        # a division by 2 represents bitwise shift by 1
        # for an even number n, if we shift the bit by 1, the number of 1s would be the same as for n // 2
        # conversely, for an odd number n, the result would be 1 + result for n // 2

        for i in range(2, n + 1):
            if i % 2:
                res.append(1 + res[i // 2])
            else:
                res.append(res[i // 2])
        
        return res