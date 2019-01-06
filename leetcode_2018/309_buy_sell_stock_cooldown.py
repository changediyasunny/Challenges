"""
309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as
you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]


Explanation:
On any i-th day, we can buy, sell or cooldown

buy[i]:
The maximum profit can be made if the first i days end with buy or wait. E.g "buy, sell, buy" or "buy, cooldown, cooldown"

sell[i]:
The maximum profit can be made if the first i days end with sell or wait. E.g "buy, sell, buy, sell" or "buy, sell, cooldown, cooldown"

price: prices[i - 1], which is the stock price of the i-th day

To calculate sell[i]:
If we sell on the i-th day, the maximum profit is buy[i - 1] + price, because we have to buy before we can sell.
If we cooldown on the i-th day, the maximum profit is same as sell[i - 1] since we did not do anything on the i-th day.
>> sell[i] is = MAX (buy[i - 1] + price, sell[i - 1])

To calculate buy[i]:
If we buy on the i-th day, the maximum profit is sell[i - 2] - price, because on the (i-1)th day we can only cooldown. If we cooldown on the i-th day, the maximum profit is same as buy[i - 1] since we did not do anything on the i-th day.
>> buy[i] is the larger one of (sell[i - 2] - price, buy[i - 1])

"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = [0] * (len(prices)+1)
        sell = [0] * (len(prices)+1)
        buy[0] = -prices[0]
        for i in range(1, len(prices)+1):
            pr = prices[i-1]
            buy[i] = max(sell[i-2]-pr, buy[i-1])
            sell[i] = max(buy[i-1]+pr, sell[i-1])
        return sell[-1]


def maxProfit_cooldown(prices):
    if len(prices) < 2:
        return 0
    # buy, sell, rest: denote profit on that day by completing activity
    buy = [0] * len(prices)
    sell = [0] * len(prices)
    rest = [0] * len(prices)

    buy[0] = -prices[0]
    for i in range(1, len(prices)):
        # profit from dont buy / rest
        buy[i] = max(buy[i-1], rest[i-1])
        # earlier buy profit + price sell today / sell on last day
        sell[i] = max(buy[i-1]+prices[i], sell[i-1])
        # sold on last day + price of today
        rest[i] = sell[i-1] + prices[i]
    return max(buy[-1], rest[-1])
