class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        intuition: if net is negative, it means the value at "sell" is smaller than value at "buy". This way we optimize for the smallest "buy" value at any given time.
        The optimization for "sell" value is obvious.
        
        O(N) time, O(1) space
        """
        max_profit = 0

        buy, sell = 0, 1
        while sell < len(prices):
            net = prices[sell] - prices[buy]
            if net < 0:
                buy = sell
            else:
                max_profit = max(max_profit, net)
            sell += 1
        
        return max_profit

        
