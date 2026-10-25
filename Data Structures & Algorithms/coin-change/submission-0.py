class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Try biggest coins first. Keep going until we reach the answer or we tried all the coins. If every branch fails, there is no right combination

        memo: dict[int, int] = {}

        if amount == 0:
            return 0

        coins.sort(reverse=True)

        def dfs(current: int):
            res = float('inf')

            if current in memo:
                return memo[current]
            if current == amount:
                return 0
            elif current > amount:
                return float('inf')
            
            for coin in coins:
                next_amount = current + coin
                _res = dfs(next_amount)
                memo[next_amount] = _res
                res = min(res, _res + 1)
            
            return res
        
        n = dfs(0)
        return n if n != float('inf') else -1

            