# Time:  O(nlog(m+n)), n is length of queries
# Space: O(n+m)

# 1409
# Given the array queries of positive integers between 1 and m, you have to process all queries[i]
# (from i=0 to i=queries.length-1) according to the following rules:
# - In the beginning, you have the permutation P=[1,2,3,...,m].
# - For the current i, find the position of queries[i] in the permutation P (indexing from 0)
# and then move this at the beginning of the permutation P. Notice that the position of queries[i]
# in P is the result for queries[i].

# Return an array containing the result for the given queries.

class BIT(object):  # Fenwick Tree, 1-indexed
    def __init__(self, n):
        self.__bit = [0] * n

    def add(self, i, val):
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def sum(self, i):
        result = 0
        while i > 0:
            result += self.__bit[i]
            i -= (i & -i)
        return result


class Solution(object):
    # 树状数组可以用来维护「单点修改」和「区间查询」两种操作
    # 对于每一个询问项query，我们想求出它在排列 P中的位置，实际上只要知道它的前面有几个数就可以
    # 把这个问题的答案转化成了一个「数数」的过程，不妨再想想题目中的操作是不是也可以往「数数」的方向上靠。
    # 每次求出query 之前有几个数之后，都需要把query 移动到数组的首部，而这样是非常不优雅的, 时间复杂度为 O(M)
    # 现实生活中管理一个队伍，想把其中的一个人放到队首，最简单的做法是直接把这个人拉出来让他/她站到第一个人的前面就行了
    # 我们知道查询的次数Q，那么我们可以使用一个长度为Q+M 的数组，一开始的排列 P占据了数组的最后 M个位置，
    # 而每处理一个询问项query，我们将其直接放到数组的前 Q个位置就行了，顺序是从右往左放置。
    # 例如对于排列[1,2,3,4,5]查询[3,1,2,1]:
    # _ _ _ _ 1 2 3 4 5
    # _ _ _ 3 1 2 _ 4 5
    # _ _ 1 3 _ 2 _ 4 5
    # _ 2 1 3 _ _ _ 4 5
    # 1 2 _ 3 _ _ _ 4 5
    # 我们发现只需要支持下面三个操作：
    # 1 查询某一个位置之前有几个位置不为空，作为返回的答案；
    # 2 将一个位置变为空；
    # 3 将一个位置变为非空。

    # 如果我们将「空」的位置看成 1，「非空」的位置看成 0，实际上就是要支持这些操作：
    #
    # 0 数组中一开始前 Q 个位置为 0，后 M 个位置为 1；
    # - 使用 M次树状数组的单点修改操作，将后面M个对应的位置变为 1。
    # 1 每次查询操作等价于询问一个前缀区间的： 可以使用树状数组的区间查询操作。
    # 2 将一个位置从 1变为 0：可以使用树状数组的单点修改操作。
    # 3 将一个位置从 0变为 1：可以使用树状数组的单点修改操作。

    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        n = len(queries)
        bit = BIT(n + m + 1)
        pos = [0] * (m + 1)
        for i in range(1, m+1):
            bit.add(n+i, 1)
            pos[i] = n+i
        ans = []
        for i, q in enumerate(queries):
            cur = pos[q]
            ans.append(bit.sum(cur-1))
            bit.add(cur, -1)

            cur = pos[q] = n - i
            bit.add(cur, 1)
        return ans

    # 模拟. 需要掌握对于变长数组的插入和删除操作
    # Time O(mn), Space O(m), , n is length of queries
    from typing import List
    def processQueries_bruteForce(self, queries: List[int], m: int) -> List[int]:
        p = [x + 1 for x in range(m)]
        ans = list()
        for query in queries:
            pos = p.index(query)
            ans.append(pos)
            p.pop(pos)
            p.insert(0, query)
        return ans


print(Solution().processQueries([3,1,2,1], 5)) # [2,1,2,1]
print(Solution().processQueries([4,1,2,2], 4)) # [3,1,2,0]
print(Solution().processQueries([7,5,5,8,3], 8)) # [6,5,0,7,5]