class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        NlogM time, M is the maximum pile
        """

        piles.sort()
        l, r = 1, max(piles)

        res = float("inf")

        while l <= r:
            rate = l + (r - l) // 2

            t = 0
            for pile in piles:
                t += math.ceil(pile / rate)
            if t <= h:
                res = min(res, rate)
                r = rate - 1
            else:
                l = rate + 1

        return res

