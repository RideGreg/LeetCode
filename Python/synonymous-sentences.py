# Time:  O(p*l * log(p*l)), p is the production of all number of synonyms
#                         , l is the length of a word
# Space: O(p*l)

# 1258 biweekly contest 13 11/16/2019
# Given a list of pairs of equivalent words synonyms and a sentence text,
# Return all possible synonymous sentences sorted lexicographically.
#
# Constraints:
#
# 0 <= synonyms.length <= 10
# synonyms[i].length == 2
# synonyms[0] != synonyms[1]
# All words consist of at most 10 English letters only.
# text is a single space separated sentence of at most 10 words.

import collections
import itertools
from typing import List

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:  # USE THIS
        groupId = dict() # {'happy':0, 'joy':0, 'sad':1, 'sorrow':1, 'cheerful':0}
        syns = []    # [['cheerful', 'happy', 'joy'], ['sad', 'sorrow']]
        for x, y in synonyms:
            if x in groupId:
                syns[groupId[x]].append(y)
                groupId[y] = groupId[x]
            elif y in groupId:
                syns[groupId[y]].append(x)
                groupId[x] = groupId[y]
            else:
                syns.append([x,y])
                groupId[x] = len(syns) - 1
                groupId[y] = len(syns) - 1

        syns = [sorted(x) for x in syns]
        #syns = list(map(sorted, syns))

        ans = []
        for w in text.split():
            idx = groupId.get(w, None)
            if idx is None:
                ans.append([w])
            else:
                ans.append(syns[idx])
        # nice to use product: product(A, B) returns the same as ((x,y) for x in A for y in B).
        # https://www.hackerrank.com/challenges/itertools-product/problem
        return [' '.join(x) for x in itertools.product(*ans)]

        '''
        ans = [[]]
        for w in text.split():
            idx = groupId.get(w, None)
            if idx is None:
                for a in ans:
                    a.append(w)
            else:
                nans = []
                for a in ans:
                    for nw in syns[idx]:
                        nans.append(a+[nw])
                ans = nans
        return [' '.join(x) for x in ans]
        #return list(map(lambda x:' '.join(x), ans))'''



# not realy need Union-Find
class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))
        self.count = n

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

class Solution_kamyu(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        def assign_id(x, lookup, inv_lookup):
            if x not in lookup:
                lookup[x] = len(lookup)
                inv_lookup[lookup[x]] = x
        
        lookup = {} # word to id
        inv_lookup = {} # id to word
        for u, v in synonyms:
            assign_id(u, lookup, inv_lookup), assign_id(v, lookup, inv_lookup)

        union_find = UnionFind(len(lookup))
        for u, v in synonyms:
            union_find.union_set(lookup[u], lookup[v])
        groups = collections.defaultdict(list)
        for i in range(len(union_find.set)):
            groups[union_find.find_set(i)].append(i) # groups is: {0: [0,1,4], 2: [2,3]}

        result = []
        for w in text.split(' '):
            if w not in lookup:
                result.append([w])
                continue
            result.append(sorted(map(lambda x: inv_lookup[x],   # sort should preprocessed and only do once
                                 groups[union_find.find_set(lookup[w])])))
        return [" ".join(sentense) for sentense in itertools.product(*result)]

print(Solution().generateSentences(
    [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
    "I am happy today but was sad yesterday"))
# ["I am cheerful today but was sad yesterday",
# ​​​​​​​"I am cheerful today but was sorrow yesterday",
# "I am happy today but was sad yesterday",
# "I am happy today but was sorrow yesterday",
# "I am joy today but was sad yesterday",
# "I am joy today but was sorrow yesterday"]