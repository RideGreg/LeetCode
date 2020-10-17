# Time:  O(nlogn), n is the number of total emails,
#                  and the max length ofemail is 320, p.s. {64}@{255}
# Space: O(n)

# 721
# Given a list accounts, each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name,
# and the rest of the elements are emails representing emails of the account.
#
# Now, we would like to merge these accounts.
# Two accounts definitely belong to the same person if there is some email
# that is common to both accounts.
# Note that even if two accounts have the same name,
# they may belong to different people as people could have the same name.
# A person can have any number of accounts initially, but all of their
# accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format:
# the first element of each account is the name, and the rest of the elements
# are emails in sorted order.
# The accounts themselves can be returned in any order.
#
# Example 1:
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
#             ["John", "johnnybravo@mail.com"],
#             ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#             ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
#           'johnsmith@mail.com'],
#          ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
#
# Explanation:
# The first and third John's are the same person as they have the common
# email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order,
# for example the answer [['Mary', 'mary@mail.com'],
#                         ['John', 'johnnybravo@mail.com'],
#                         ['John', 'john00@mail.com', 'john_newyork@mail.com',
#                          'johnsmith@mail.com']]
# would still be accepted.
#
# Note:
#
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].

import collections

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

# UnionFind on account (rather than emails which is too many)
class Solution():
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def union(x, y):
            print("union {} {}".format(x, y))
            xroot, yroot = find(x), find(y)
            if xroot != yroot:
                pid[max(xroot, yroot)] = min(xroot, yroot)

        def find(x):
            if pid[x] != x:
                pid[x] = find(pid[x])
            return pid[x]

        N = len(accounts)
        pid, email2id = list(range(N)), {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email2id:
                    # duplicate email triggers union
                    union(i, email2id[email])
                else:
                    # new email adds to hash
                    email2id[email] = i

        # group emails to single id
        emaillist = collections.defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                emaillist[find(i)].add(email)

        return [[accounts[id][0]] + sorted(emaillist[id]) for id in emaillist]


# DFS 如果两个电子邮件出现在同一个帐户中，则在它们之间连一条边。那么问题归结为找到这个图的连接组件（每个连通子图算一个组件）。
# 具体算法：对于每个帐户，从第一个电子邮件到每个电子邮件画一条边。然后使用深度优先搜索合并相同的账户。
class Solution(object):
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                graph[acc[1]].add(email) # KENG: 要连一条边指向自身，不然不会出现在graph中
                #graph[email].add(acc[1])

        seen, ans = set(), []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email] # prepare for DFS
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans


print(Solution().accountsMerge([
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"]
])) # ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]