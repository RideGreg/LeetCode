class Solution:
    def maximumAssociationSet(self, ListA, ListB):
        class UnionFind(object):
            def __init__(self, n):
                self.set = range(n)
                self.size = [1]*n
                self.maxSize = 1
                self.maxId = 0

            def find_set(self, x):
                if self.set[x] != x:
                    self.set[x] = self.find_set(self.set[x])  # path compression.
                return self.set[x]

            def union_set(self, x, y):
                x_root, y_root = map(self.find_set, (x, y))
                if x_root != y_root:
                    smallRoot, largeRoot = min(x_root, y_root), max(x_root, y_root)
                    self.set[smallRoot] = largeRoot
                    self.size[largeRoot] += self.size[smallRoot]
                    if self.size[largeRoot] > self.maxSize:
                        self.maxSize = self.size[largeRoot]
                        self.maxId = largeRoot

            lookup, id = {}, 0
            total = set(ListA).union(ListB)
            for book in total:
                lookup[book] = id
                id += 1

            circles = UnionFind(len(total))
            for idx, a in enumerate(ListA):
                i, j = lookup[a], lookup[ListB[idx]]
                circles.union_set(i, j)

            ans = []
            for book in total:
                if circles.find_set(lookup[book]) == circles.maxId:
                    ans.append(book)
            return ans

print Solution().maximumAssociationSet(["abc","abc","abc"],["bcd","acd","def"])
print Solution().maximumAssociationSet(["a","b","d","e","f"], ["b","c","e","g","g"])
