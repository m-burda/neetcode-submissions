class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # at each step, we can choose one of the coins
        # brute force dfs won't work because we're looking for combinations, not permutations
        # we can either choose or skip a current coin
        # by skipping we're moving the index forward, ensuring we do not create permutations with coins that come before <i>

        memo = {}
        
        def dfs(i: int, target:int):
            if (i, target) in memo:
                return memo[(i, target)]
            if i >= len(coins):
                return 0
            if target == 0:
                return 1
            elif target < 0:
                return 0
            
            pick = dfs(i, target - coins[i])
            skip = dfs(i + 1, target)

            memo[(i, target)] = pick + skip

            return pick + skip

        return dfs(0, amount)