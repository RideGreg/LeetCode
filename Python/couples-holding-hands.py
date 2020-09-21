# Time:  O(n)
# Space: O(n)

# 765
# N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps
# so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.
#
# The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order,
# the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
#
# The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

# len(row) is even and in the range of [4, 60].
# row is guaranteed to be a permutation of 0...len(row)-1.



#
#
class Solution(object):
    # Union Find:
    # 设想一下加入有两对情侣互相坐错了位置，我们至多只需要换一次。
    # 如果三对情侣相互坐错了位置，A1+B2,B1+C2,C1+A2。他们三个之间形成了一个环，我们只需要交换两次。
    # 如果四队情侣相互坐错了位置，即这四对情侣不与其他情侣坐在一起，A1+B2,B1+C2,C1+D2,D1+A2.他们四个之间形成了一个环，他们只需要交换三次并且不用和其他情侣交换，就可以将这四对情侣交换好，
    # 以此类推，其实就是假设k对情侣形成一个环状的错误链，我们只需要交换k - 1次就可以将这k对情侣的位置排好。
    # 所以问题转化成N对情侣中，有几个这样的错误环。假设m个环，各有k1, k2 .. km人
    # 交换次数 (k1-1) + (k2-1) ... + (km-1) = N - m
    #
    # 可用并查集来解决，每次遍历相邻的两个位置，如果他们本来就是情侣，他们处于大小为1的错误环中，只需要交换0次。
    # 如果不是情侣，说明他们呢两对处在同一个错误环中，将他们合并（union），将所有的错坐情侣合并和后，答案就是情侣对 - 环个数。
    # 举例，最差的情况就是所有N对情侣都在一个环中，这时候我们需要N - 1调换。
    # 最好情况每对情侣已经坐好了，已经有N个大小为1的环，这时候我们需要N - N次调换。
    # 也可以看总共union了多少次，这就是需要交换回来的次数。
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                self.ans += 1
                root[max(rx, ry)] = min(rx, ry)

        root = [x if x % 2 == 0 else x-1 for x in range(len(row))]
        self.ans = 0
        for i in range(0, len(row), 2):
            union(row[i], row[i + 1])  # if they are couple, union is no-op
        return self.ans


    # Graph Search
    # 首先可以把题目中给出表示情侣的数组对 (0, 1), (2, 3), (4, 5), ... 用 (0, 0), (1, 1), (2, 2), ...
    # 来表示，这种转换是不会影响答案的。再想象一下有 N 个两人沙发，编号为 0, 1, 2, ..., N-1。
    # 这就可以把问题转换成让每对情侣坐在一张沙发上至少需要多少次交换。如果一对情侣不坐在一对沙发上，
    # 那么就有两种交换的选择将这张沙发上凑成一对情侣。对于这样的交换，其实可以把它化成一张图，
    # 举个例子，情侣坐在沙发 X 和 Y(可能是同一个沙发），可以画一条 X 到 Y 的无向边来表示 X 沙发
    # 跟 Y 沙发上可以组成一对情侣。这样最后画成的图每个节点的度为2，图上有一些连通分量。
    #
    # 每次将一个沙发上凑成一对情侣之后，在图上的变化是多了一个自循环的连通分量。我们的目标是让
    # 图中有 N 个自循环连通分量，每个连通分量代表一对情侣。每次交换都会将连通分量的数量增加 1，
    # 问题的答案可以通过 N 减去最开始情侣图中自循环连通分量的个数来得到。
    def minSwapsCouples2(self, row):
        N = len(row)//2
        couples = [[] for _ in range(N)]
        # 人编号转化为couples 0,1,...N-1，记录他们在0,1...N-1双人沙发的座号
        for seat, num in enumerate(row):
            couples[num//2].append(seat//2)
        # 每队couple坐于couch1, couch2，连一条无向边
        adj = [[] for _ in range(N)]
        for couch1, couch2 in couples:
            adj[couch1].append(couch2)
            adj[couch2].append(couch1)

        ans = 0
        for start in range(N):
            if not adj[start]: continue
            x, y = start, adj[start].pop()
            # if y == start, means 换到start沙发上的正好组成couple，可以看下一个沙发
            # 如果 y != start, 与y沙发上某人交换 adj[y].pop()
            while y != start:
                ans += 1
                adj[y].remove(x)
                x, y = y, adj[y].pop() # 这个y是将要换到start沙发上的人
        return ans  # also equals to N - (# of cycles)

        ''' # Answer is N minus the number of cycles in "adj"
        ans = N
        for start in range(N):
            if not adj[start]: continue
            ans -= 1
            x, y = start, adj[start].pop()
            while y != start:
                adj[y].remove(x)
                x, y = y, adj[y].pop()
        return ans
        '''

    # Greedy: Time O(n^2), Space O(1)
    # The couple of person x is x^1. For persons on seat 0,2,4... find his couple and exchange.
    def minSwapsCouples3(self, row):
        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            if row[i+1] != x^1:
                ans += 1
                for j in range(i+2, len(row)):
                    if row[j] == x^1:
                        row[i+1], row[j] = row[j], row[i+1]
                        break
        return ans


print(Solution().minSwapsCouples([5,0,3,1,4,2])) # 2
print(Solution().minSwapsCouples([2,3,4,5,0,1])) # 0