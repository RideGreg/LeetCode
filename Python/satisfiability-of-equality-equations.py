# Time:  O(n)
# Space: O(1)

# 990
# Given an array equations of strings that represent relationships between variables, each string
# equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b
# are lowercase letters (not necessarily different) that represent one-letter variable names.
#
# Return true if and only if it is possible to assign integers to variable names so as to satisfy
# all the given equations.

# Input: ["a==b","b!=c","c==a"]
# Output: false

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        union_find = UnionFind(26)
        for eqn in equations:
            x = ord(eqn[0]) - ord('a')
            y = ord(eqn[3]) - ord('a')
            if eqn[1] == '=':
                union_find.union_set(x, y)
        for eqn in equations:
            x = ord(eqn[0]) - ord('a')
            y = ord(eqn[3]) - ord('a')
            if eqn[1] == '!':
                if union_find.find_set(x) == union_find.find_set(y):
                    return False
        return True


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph = [[] for _ in xrange(26)]

        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        color = [None]*26
        c = 0
        for start in xrange(26):
            if color[start] is not None:
                continue
            c += 1
            stack = [start]
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if color[nei] is None:
                        color[nei] = c
                        stack.append(nei)

        for eqn in equations:
            if eqn[1] == '!':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                if x == y: # this is required for ['a!=a'] to be correct, which is not in graph and not colored.
                    return False
                if color[x] == color[y] and color[x] is not None:
                    return False
        return True

print(Solution2().equationsPossible(["a==b","b!=c","c==a"])) # False
print(Solution2().equationsPossible(["a!=a"])) # False