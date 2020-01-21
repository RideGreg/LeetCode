# Time:  O(nlogn)
# Space: O(n)

# 1202 weekly contest 155 9/21/2020

# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b]
# indicates 2 indices(0-indexed) of the string.
#
# You can swap the characters at any pair of indices in the given pairs any number of times.
#
# Return the lexicographically smallest string that s can be changed to after using the swaps.

import collections


class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[max(x_root, y_root)] = min(x_root, y_root)
        return True


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        groups = UnionFind(len(s))
        for x,y in pairs: 
            groups.union_set(x, y)

        components = collections.defaultdict(list)
        for i in range(len(s)):
            id = groups.find_set(i)
            components[id].append(s[i])  # store char, index is no longer useful
        for comp in components.values():
            comp.sort(reverse=True)

        ans = []
        for i in range(len(s)):
            c = components[groups.find_set(i)].pop() # 倒排技术，可逐个consume
            ans.append(c)
        return "".join(ans)

        ''' # 如不会倒排技术，就一次性把一个union全写入。坏处是需要维护两套list，一套是位置id，另一套是字符。
        d = collections.defaultdict(list)
        for i in range(len(s)):
            id = groups.find_set(i)
            d[id].append(i)

        ss = ['']*len(s)
        for v in d.values():
            charset = [s[j] for j in v]
            charset.sort()
            for idx, char in zip(v, charset):  # pythonic way to join two lists by index
                ss[idx] = char
        return ''.join(ss)
        '''

# Time:  O(nlogn)
# Space: O(n)
import itertools
class Solution2(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        def dfs(i):
            lookup.add(i)
            component.append(i)
            for j in adj[i]:
                if j not in lookup:
                    dfs(j)
            
        adj = collections.defaultdict(list)
        for i, j in pairs:
            adj[i].append(j)
            adj[j].append(i)
        lookup = set()
        result = list(s)
        for i in range(len(s)):
            if i in lookup:
                continue
            component = []
            dfs(i)
            component.sort()
            chars = sorted(result[k] for k in component)
            for comp, char in zip(component, chars):
                result[comp] = char
        return "".join(result)

print(Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2]])) # 'bacd'
print(Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]])) # 'abcd'
print(Solution().smallestStringWithSwaps("cba", [[0,1],[1,2]])) # 'abc'
