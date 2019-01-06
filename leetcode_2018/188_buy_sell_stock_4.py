"""
188. Best Time to Buy and Sell Stock IV

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

DP running time: O(days * transctions)
https://www.youtube.com/watch?v=oDhu5uGq_ic

"""
def maxProfit_dp(prices, k=2):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    days = len(prices)
    trans = k + 1

    dp = [[0] * days for _ in range(k+1)]
    for tr in range(1, k+1):
        maxdiff = -prices[0]
        for dy in range(1, days):
            # no-transactoin-at-all OR diff until m days
            dp[tr][dy] = max(dp[tr][dy-1], maxdiff + prices[dy])
            maxdiff = max(maxdiff, dp[tr-1][dy] - prices[dy])
            # max([(prices[day] - prices[m] + T[transaction - 1][m]) for m in range(day)]))
    pp.pprint(dp)
    return dp[-1][-1]

def maxProfit(prices, k=2):
    if not prices:
        return 0
    r_profits = [0] * len(prices)
    for tr in range(k):
        tr_profit = 0
        for i in range(1, len(prices)):
            curr_profit = prices[i] - prices[i-1]
            tr_profit = max(r_profits[i], tr_profit+curr_profit)
            r_profits[i] = max(r_profits[i-1], tr_profit)
    return r_profits[-1]

prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
maxProfit(prices)
