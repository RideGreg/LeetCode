import heapq
class Solution:
    def topKMovie(self, rating, G, S, K):
        class UnionFind(object):
            def __init__(self, n):
                self.set = range(n)
                self.count = n

            def find_set(self, x):
                if self.set[x] != x:
                    self.set[x] = self.find_set(self.set[x])  # path compression.
                return self.set[x]

            def union_set(self, x, y):
                x_root, y_root = map(self.find_set, (x, y))
                if x_root != y_root:
                    self.set[min(x_root, y_root)] = max(x_root, y_root)
                    self.count -= 1

        circles = UnionFind(len(rating))
        for i, g in enumerate(G):
            for j in g:
                circles.union_set(i, j)

        gId = circles.find_set(S)
        ans = []
        for i, rat in enumerate(rating):
            if i != S and circles.find_set(i) == gId:
                ans.append((rat, i))
        return [i[1] for i in heapq.nlargest(K, ans)]

print Solution().topKMovie([10,20,30,40],  [[1,3],[0,2],[1],[0]],  0, 2)
print Solution().topKMovie([10,20,30,40,50,60,70,80,90], [[1,4,5],[0,2,3],[1,7],[1,6,7],[0],[0],[3],[2,3],[]], 5, 3,)
