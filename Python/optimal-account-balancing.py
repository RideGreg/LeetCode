# Time:  O(n * 2^n), n is the size of the debt.
# Space: O(2^n)

# 465
# A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for 10.
# Then later Chris gave Alice 5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x
# gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID),
# the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
#
# Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.
#
# Note:
# 1. A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
# 2. Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.

import collections


class Solution(object):
    # backtracking O(n!)
    #
    # use backtracking and greedy to clear each person's debts from 1st person till last one.
    # How to clear one person's debt? find a person 2 after him that has opposite sign(+->-  or - -> +), and clear
    # person1's whole debt with person2 only.
    # Here's the trick: example: [7, -6, -1], one obvious optimal solution is person1 pay $6 to person2, and pay $1 to person3.
    # Notice this is equivalent to another solution: person1 pay $7 to person2, and person2 pay $1 to person3.
    # So when doing DFS, everytime we only consider clearing person1's debt wholly with another 1 person, we don't need
    # to consider clearing with other more people, cause clearing with 1 person is already guaranteed to be optimal.
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        accounts = collections.defaultdict(int)
        for s, d, v in transactions:
            accounts[s] += v
            accounts[d] -= v

        debts = [a for a in accounts.values() if a]

        def dfs(pos):
            while pos < len(debts) and debts[pos] == 0: # go to next pos if already clear in previous swaps
                pos += 1
            if pos == len(debts):
                return 0

            ans = float('inf')
            for i in range(pos+1, len(debts)):
                if debts[pos] * debts[i] < 0:
                    debts[i] += debts[pos]
                    ans = min(ans, 1 + dfs(pos+1))
                    debts[i] -= debts[pos]
            return ans

        return dfs(0)




    def minTransfers_kamyu(self, transactions): # O(n * 2^n), but hard to understand
        accounts = collections.defaultdict(int)
        for s, d, v in transactions:
            accounts[s] += v
            accounts[d] -= v

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
        for i in range(len(dp)):
            for j in range(len(debts)):
                if (i & (1<<j)) == 0:
                    nxt = i | (1<<j)
                    sums[nxt] = sums[i]+debts[j]
                    if sums[nxt] == 0:
                        dp[nxt] = max(dp[nxt], dp[i]+1)
                    else:
                        dp[nxt] = max(dp[nxt], dp[i])
        return len(debts)-dp[-1]


    # 统计每个人借出/借入的金钱总数
    # 将借出金钱的人放入集合rich，借入金钱的人放入集合poor
    # 问题转化为计算从rich到poor的最小“债务连线”数
    # 尝试用rich中的每个金额与poor中的每个金额做匹配
    # 若存在差值，则将差值加入相应集合继续搜索
    # 通过保存中间计算结果可以减少重复搜索
    def minTransfers_bookshadow(self, transactions):
        vdict = collections.defaultdict(dict)

        def solve(rich, poor):
            rlen, plen = len(rich), len(poor)
            if min(rlen, plen) <= 1:
                return max(rlen, plen)
            rich.sort()
            poor.sort()
            trich, tpoor = tuple(rich), tuple(poor)
            ans = vdict[trich].get(tpoor)
            if ans is not None:
                return ans
            ans = 0x7FFFFFFF
            for ri in range(rlen):
                nrich = rich[:ri] + rich[ri+1:]
                npoor = poor[1:]
                if rich[ri] < poor[0]:
                    npoor.append(poor[0] - rich[ri])
                elif rich[ri] > poor[0]:
                    nrich.append(rich[ri] - poor[0])
                ans = min(solve(nrich, npoor) + 1, ans)
            vdict[trich][tpoor] = ans
            return ans

        loan = collections.defaultdict(int)
        for s, t, v in transactions:
            loan[s] += v
            loan[t] -= v
        rich = [v for k, v in loan.items() if v > 0]
        poor = [-v for k, v in loan.items() if v < 0]
        return solve(rich, poor)


print(Solution().minTransfers([[0,1,10], [2,0,5]])) # 2. One way to settle is person #1 pay #0 and #2 $5 each.
print(Solution().minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])) # 1