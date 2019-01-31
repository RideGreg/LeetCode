# Time:  O(f * n), f is the max number of unique prime factors
# Space: O(p + n), p is the total number of unique primes

# 952
# Given a non-empty array of unique positive integers A, consider the following graph:
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.

# Return the size of the largest connected component in the graph.


# Solution: Union-Find + prime factor decomposition. Doing n^2 times gcd will TLE.


import collections


class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.size = [1]*n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.size[max(x_root, y_root)] += self.size[min(x_root, y_root)]
        return True


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def primeFactors(i):  # prime factor decomposition
            result = []
            d = 2
            while d*d <= i:
                if i%d == 0:
                    while i%d == 0:
                        i //= d
                    result.append(d)
                d += 1
            if i > 1:
                result.append(i)
            return result
        
        union_find = UnionFind(len(A))
        nodesWithCommonFactor = {}
        for i in xrange(len(A)):
            for factor in primeFactors(A[i]):
                if factor not in nodesWithCommonFactor:
                    nodesWithCommonFactor[factor] = i
                else:
                    union_find.union_set(nodesWithCommonFactor[factor], i)
        return max(union_find.size)

print(Solution().largestComponentSize([4,6,15,35]))
print(Solution().largestComponentSize([20,50,9,63]))
print(Solution().largestComponentSize([2,3,6,7,4,12,21,39]))