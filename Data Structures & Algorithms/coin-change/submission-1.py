class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # DP bottom-up solution
        # Solve subproblems for each amount starting from 0 up to <amount>
        # At each step, we compute the minimum number of coins for the current amount by iterating over available coins and using previously computed results
        # The last step is the answer
        # We already know the answer for amount = 0
        # Time complexity O(A*C); space complexity O(A), where A is amount, C is number of coins

        results = [float("inf")] * (amount + 1)
        results[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    results[a] = min(results[a], 1 + results[a - coin])
        
        return results[-1] if results[-1] != float("inf") else -1

            