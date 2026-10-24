class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # cost of reaching i + 1 from i is 20. This is already the minimal cost
        # min cost of reaching i + 1 from i - 1 is 15. Already minimal
        # cost of reaching i + 1 from i - 2 is 10 + 15 -> 25
        # min cost of reaching i + 1 from start (from index 0 or 1) = min(15, 25) -> 15

        if len(cost) > 2:
            for i in range(len(cost) - 3, -1, -1):
                cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
        
        print(cost)
        return min(cost[0], cost[1])