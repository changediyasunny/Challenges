"""
465. Optimal Account Balancing

A group of friends went on holiday and sometimes lent each other money. For example,
Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride.
We can model each transaction as a tuple (x, y, z) which means person x gave person y $z.
Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are
the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number
of transactions required to settle the debt.

Input:
[[0,1,10], [2,0,5]]
Output:
2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
Output:
1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.

Solution:
First we need to count the net balance for every person, we define it as the list "net".
The question is the same as finding the "loop" in a graph (which the sum of elements in
each graph is 0), say, the answer is len(net) - number of circles.

This can be converted into finding the minimal clique such that the elements sum up to
be zero. Minimal means there is no subset which sums up to zero. In the example above,
there are two minimal such cliques.

"""

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """

        def remove_zero_clique(debts):
            while stack:
                t, path, start = stack.pop(0)
                if not t:
                    break
                for k in range(start, len(debts)):
                    stack.append((t+debts[k], path + [k], k+1))
            paths = set(path)
            return [debts[i] for i in range(len(debts)) if i not in paths]
        # build debts data
        data = collections.defaultdict(int)
        for src, dest, price in transactions:
            data[src] += -price
            data[dest] += price
        # remove zero balance entries
        debts = [data[item] for item in data if data[item] != 0]
        total_cnt = len(debts)
        # number of transactions is len(debts) - zero_cliques
        while len(debts) > 0:
            # price, path, start
            stack = [(debts[0], [0], 1)]
            debts = remove_zero_clique(debts)
            total_cnt -= 1
        return total_cnt
