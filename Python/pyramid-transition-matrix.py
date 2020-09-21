# Time:  O((a^(b+1)-a)/(a-1)) = O(a^b) , a is the size of allowed,
#                                        b is the length of bottom
# Space: O((a^(b+1)-a)/(a-1)) = O(a^b)

# We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.
#
# For every block of color `C` we place not in the bottom row,
# we are placing it on top of a left block of color `A` and right block of color `B`.
# We are allowed to place the block there only if `(A, B, C)` is an allowed triple.
#
# We start with a bottom row of bottom, represented as a single string.
# We also start with a list of allowed triples allowed.
# Each allowed triple is represented as a string of length 3.
#
# Return true if we can build the pyramid all the way to the top, otherwise false.
#
# Example 1:
# Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
#     A
#    / \
#   D   E
#  / \ / \
# X   Y   Z
#
# This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
# Example 1:
# Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
#
# Note:
# bottom will be a string with length in range [2, 100].
# allowed will have length in range [0, 350].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.

import collections, itertools
# dfs solution
class Solution(object):
    def pyramidTransition(self, bottom, allowed):  # USE THIS
        def dfs(s):
            if len(s) == 1:
                return True

            #for i in product(*(lookup[a, b] for a, b in zip(s, s[1:]))):
            cands = []
            for i in range(1, len(s)):
                if (s[i-1], s[i]) not in lookup:
                    return False
                cands.append(lookup[s[i-1], s[i]])

            for nxt in itertools.product(*cands):
                if dfs(nxt):
                    return True
            return False

        lookup = collections.defaultdict(set)
        for a, b, c in allowed:
            lookup[a, b].add(c)

        return dfs(bottom)


    # BFS: TLE. Search all possibilities takes longer time, dfs can return faster.
    def pyramidTransition_TLE(self, bottom, allowed):
        lookup = collections.defaultdict(set)
        for s in allowed:
            lookup[s[:2]].add(s[2])

        q = [bottom]
        while q:
            nextq = set() # list could have a lot of duplicates -> TLE
            for s in q:
                cur = ['']
                for i in range(1, len(s)):
                    if s[i - 1:i + 1] not in lookup:
                        break
                    cur = [pre + cand for pre in cur for cand in lookup[s[i - 1:i + 1]]]
                else:
                    nextq.update(cur)

            if not nextq:
                return False
            if len(next(iter(nextq))) == 1: return True
            q = list(nextq)
        return False


    # DFS: use generator to supply next level, hard to remember
    def pyramidTransition2(self, bottom, allowed):
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        # Comments can be used to cache intermediate results
        seen = set()
        def dfs(A):
            if len(A) == 1: return True
            if A in seen: return False
            seen.add(A)
            return any(dfs(cand) for cand in build(A, []))

        def build(A, ans, i=0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i + 1]]:
                    ans.append(w)
                    for result in build(A, ans, i + 1):
                        yield result
                    ans.pop()

        return dfs(bottom)


    # don't use: pyramidTransitionHelper() and dfs() calls each other. It works because each
    # recursive call with shorter param, but hard to understand
    def pyramidTransition_kamyu(self, bottom, allowed):
        def pyramidTransitionHelper(bottom, edges, lookup):
            def dfs(bottom, new_bottom, idx, lookup):
                if idx == len(bottom)-1:
                    return pyramidTransitionHelper("".join(new_bottom), edges, lookup)
                for i in edges[ord(bottom[idx])-ord('A')][ord(bottom[idx+1])-ord('A')]:
                    new_bottom[idx] = chr(i+ord('A'));
                    if dfs(bottom, new_bottom, idx+1, lookup):
                        return True
                return False

            if len(bottom) == 1:
                return True
            if bottom in lookup:
                return False
            lookup.add(bottom)
            for i in range(len(bottom)-1):
                if not edges[ord(bottom[i])-ord('A')][ord(bottom[i+1])-ord('A')]:
                    return False
            new_bottom = ['A']*(len(bottom)-1)
            return dfs(bottom, new_bottom, 0, lookup)

        edges = [[[] for _ in range(7)] for _ in range(7)]
        for s in allowed:
            edges[ord(s[0])-ord('A')][ord(s[1])-ord('A')].append(ord(s[2])-ord('A'))
        return pyramidTransitionHelper(bottom, edges, set())



print(Solution().pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"])) # True
print(Solution().pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"])) # False
print(Solution().pyramidTransition("DBCBBC",
["AAD","ACB","AAA","AAC","AAB","BCD","BCA","BCC","BAB","BAC","BAA","CAC","CAB","CAA","CCC",
 "DAD","BDD","CCD","DAA","DAC","ACD","DCC","ACC","ABA","ABB","ABC","ABD","BDC","BDB","BBD",
 "BBC","BBB","ADD","ADB","ADC","ADA","DDC","DDA","CBB","CBC","CBA","CDA","CBD","CDC","DBA","DBC"]))
# True