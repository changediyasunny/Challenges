"""
714. Best Time to Buy and Sell Stock with Transaction Fee

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

running time: O(N)

At the end of the i-th day, we maintain "sell", the maximum profit we could have if we did
not have a share of stock, and "buy", the maximum profit we could have if we owned a share of stock.

To transition from the i-th day to the i+1-th day, we either
>> sell our stock "sell" = max("sell", "buy" + prices[i] - fee) or
>> buy a stock "buy" = max("buy", "sell" - prices[i]). At the end, we want to return "sell".
We can transform "sell" first without using temporary variables because selling and buying
on the same day can't be better than just continuing to "buy" the stock.

"""


class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            sell = max(sell, buy + prices[i] - fee)
            buy = max(buy, sell-prices[i])
        return sell

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1], sell[i-1]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)
        # print(buy)
        # print(sell)
        return sell[-1]
