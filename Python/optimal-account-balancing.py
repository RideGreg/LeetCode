# Time:  O(n * 2^n), n is the size of the debt.
# Space: O(2^n)

import collections


class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        accounts = collections.defaultdict(int)
        for transaction in transactions:
            accounts[transaction[0]] += transaction[2]
            accounts[transaction[1]] -= transaction[2]

        debts = [account for account in accounts.values() if account]
            
        if not debts:
            return 0

        '''
        n = 1 << len(debts)
        dp, subset = [float("inf")] * n, []
        for i in xrange(1, n):
            net_debt, number = 0, 0
            for j in xrange(len(debts)):
                if i & 1 << j:
                    net_debt += debts[j]
                    number += 1
            if net_debt == 0:
                dp[i] = number - 1
                for s in subset:
                    if (i & s) == s:
                        dp[i] = min(dp[i], dp[s] + dp[i - s])
                subset.append(i)
        return dp[-1]
        '''

        dp = [0]*(2**len(debts))
        sums = [0]*(2**len(debts))
        for i in xrange(len(dp)):
            for j in xrange(len(debts)):
                if (i & (1<<j)) == 0:
                    nxt = i | (1<<j)
                    sums[nxt] = sums[i]+debts[j]
                    if sums[nxt] == 0:
                        dp[nxt] = max(dp[nxt], dp[i]+1)
                    else:
                        dp[nxt] = max(dp[nxt], dp[i])
        return len(debts)-dp[-1]
