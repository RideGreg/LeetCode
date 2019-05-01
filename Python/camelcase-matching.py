# Time:  O(n * l), n is number of quries
#                , l is length of query
# Space: O(1)

# 1023
# A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals
# the query. (We may insert each character at any position, and may insert 0 characters.)
#
# Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true
# if and only if queries[i] matches the pattern.

class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def is_matched(query, pattern):
            i = 0
            for c in query:
                if i < len(pattern) and pattern[i] == c:
                    i += 1
                elif c.isupper():
                    return False
            return i == len(pattern)
        
        return [is_matched(query, pattern) for query in queries]

    def camelMatch_lee215(self, qs, p):
        def u(s):
            return [c for c in s if c.isupper()]

        def issup(s, t):
            it = iter(t)
            return all(c in it for c in s)
        return [u(p) == u(q) and issup(p, q) for q in qs]

print(Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], 'FoBa'))
# [true,false,true,false,false]
