import functools

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # memoized dfs with three choices: buy, sell, skip

        @functools.cache
        def dfs(i: int, buying: bool, cooldown: bool = False):
            if i > len(prices) - 1:
                return 0
            
            price = prices[i]

            buy, sell = 0, 0
            skip = dfs(i + 1, buying)
            if not cooldown:
                if not buying:
                    buy = dfs(i + 1, True) - price
                else:
                    sell = dfs(i + 1, False, True) + price

            return max(buy, skip, sell)
        
        return dfs(0, 0)