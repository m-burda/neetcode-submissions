class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # let's try to solve this bottom-up instead of top-down now
        # define a matrix amount x len(coins)
        # we can either choose or skip a given coin at any time
        # at any time, our current position describes a different subproblem. For example, if we have amount = 5, coins = [1, 2, 5], we would have a matrix with rows 1,2,5 and target 5, 4, 3, 2, 1, 0
        # if we draw a project to x from our current sell, the line designates the start of our subproblem. For example, if we decide to choose coin 1 on first step, we mode to the right. This way, our projection y still points at [1,2,5] coins, but our target is now 5 - 1 = 4
        # Similarly, if we decide to skip the coin, we go down instead of right - the target stays the same, but our choice of coins is reduced to [2,5]
        # This is because we will traverse in reverse and add up all results from the neighboring cells (namely the right and bottom cells relative to our current cell)
        # we add a padding column to the right where target is 0 and all the values are 1. This is because if 0 is reachable from any current cell, we have 1 correct combination already
        # we compute each cell by adding cell[r + 1][c] and cell[r][c + r]. These cells answer the question for "how many ways are there to reach the target in cases where we pick this coin" and "where we skip this coin"
        # when we reach the first cell, we will have all possible combinations added up for the whole problem

        # This has O(A * C) time and O(A * C) space, where A is the amount and C is the number of coins
        # We can further optimize space to be O(A), by only using two rows. This is because to compute answers we only need the current row and the immediate bottom one

        grid = [[0] * (amount + 1) for _ in range(len(coins))]

        for r in range(len(coins)):
            grid[r][-1] = 1
        
        for r in range(len(coins) - 1, -1, -1):
            for target in range(amount - 1, -1, -1):
                # this operation conceptually designates amount - coin, but since our amounts are reversed relatively to the indices we have to add those instead
                # e.g., at index 5 our amount is 0, and at index 0 our amount is 5
                coin = coins[r]
                if coin <= amount - target:
                    pick = grid[r][coin + target]
                else:
                    pick = 0
                
                if r + 1 < len(coins):
                    skip = grid[r + 1][target]
                else:
                    skip = 0

                grid[r][target] = pick + skip 

        return grid[0][0]