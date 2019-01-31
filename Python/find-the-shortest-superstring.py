# Time:  O(n^2 * (l^2 + 2^n)). leetcode says O(n^2 * (w + 2^n)) where n is # of words, w is max length of each word
# Space: O(n^2). leetcode says O(n * (w + 2^n))

# 943
# Given an array A of strings, find any smallest string that contains each string in A as a substring.
# We may assume that no string in A is substring of another string in A.
# 1 <= A.length <= 12
# 1 <= A[i].length <= 20

# Dynamic Programming:
# We have to put all words into a row, where each word may overlap the previous word. Because no word is contained in another word.
#
# It is equal to maximize the total overlap of the words. Say we have put some words down in our row, ending with
# word A[i]. Now say we put down word A[j] as the next word, where word j hasn't been put down yet. The overlap
# increases by overlap(A[i], A[j]).
#
# Use Dynamic Programming is to store the concatenated strings, until all word are used. This is doable since the # of
# words and length of each word is small.

# Another way to use dynamic programming: let dp(mask, i) be the total overlap after putting some words down
# (represented by a bitmask, e.g. mask 7 means words 0,1,2), for which A[i] was the last word put down. Then, the key
# recursion is dp(mask ^ (1<<j), j) = max(overlap(A[i], A[j]) + dp(mask, i)), where i can be one of the bits set in mask,
# and the jth bit is newly added to mask (i.e. word j is concatenated after word i).
#
# This only tells us what the maximum overlap is for each set of words. We also need to remember each choice along the way
# (ie. the specific i that made dp(mask ^ (1<<j), j) achieve a maximum) so that we can reconstruct the answer.
#
# Algorithm
# 3 main components:
# - Precompute overlap(A[i], A[j]) for all possible i, j.
# - Calculate dp[mask][i], keeping track of the "parent" i for each j as described above.
# - Reconstruct the answer using parent information.


class Solution(object):
    def shortestSuperstring(self, A): # USE THIS
        """
        :type A: List[str]
        :rtype: str
        """
        n = len(A)
        # Populate overlaps
        overlaps = [[0]*n for _ in xrange(n)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i == j: continue
                for l in xrange(min(len(x), len(y)), 0, -1):
                    if x.endswith(y[:l]):
                        overlaps[i][j] = l
                        break

        # dp[mask][i] = shortest string by concatenating some words (represented by a bitmask mask) and
        # A[i] was the last word.
        dp = [['']*n for _ in xrange(1<<n)]
        # traverse the dp matrix
        for mask in xrange(1, 1<<n):
            for bit in xrange(n):
                if (mask>>bit) & 1: # mask contains this bit, e.g. mask 7 contains bit 0,1,2.
                    prev_mask = mask ^ (1<<bit) # remove current bit from mask
                    if prev_mask == 0:
                        dp[mask][bit] = A[bit]
                        continue

                    for i in xrange(n):
                        if (prev_mask>>i) & 1:
                            overlap = overlaps[i][bit]
                            s = dp[prev_mask][i] + A[bit][overlap:]
                            if not dp[mask][bit] or len(s)<len(dp[mask][bit]):
                                dp[mask][bit] = s

        return min(dp[-1], key=len)

    def shortestSuperstring_LeetCodeOfficial(self, A):
        n = len(A)

        # Populate overlaps
        overlaps = [[0]*n for _ in xrange(n)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i == j: continue
                for l in xrange(min(len(x), len(y)), 0, -1):
                    if x.endswith(y[:l]):
                        overlaps[i][j] = l
                        break

        # dp[mask][i] = total overlap saving after putting some words down (represented by a bitmask mask),
        # for which A[i] was the last word put down.
        dp = [[0]*n for _ in xrange(1<<n)]
        prev = [[None]*n for _ in xrange(1<<n)]
        # traverse the dp matrix
        for mask in xrange(1, 1<<n):
            for bit in xrange(n):
                if (mask>>bit) & 1: # mask contains this bit, e.g. mask 7 contains bit 0,1,2.
                    # Let's try to find dp[mask][bit]. We should already have
                    # a collection of items represented by prev_mask, which has less digits than mask.
                    prev_mask = mask^(1<<bit) #remove current bit from mask
                    if prev_mask == 0: continue #if prev is empty string, skip for finding overlap

                    for i in xrange(n):
                        if (prev_mask>>i) & 1:
                            # prev_mask contains this bit. For each bit i in prev_mask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[prev_mask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]: # this is done only when there is more overlap
                                dp[mask][bit] = value
                                prev[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Follow parents backwards path that retains maximum overlap to reconstruct answer.
        bit = max(xrange(n), key=lambda x: dp[-1][x])
        #equivalent: bit = max(xrange(n), key = dp[-1].__getitem__)
        idx = []
        mask = (1<<n)-1  # all bits on
        while bit is not None:
            idx.append(bit)
            mask, bit = mask^(1<<bit), prev[mask][bit]

        # Reverse path to get forwards direction; add all remaining words which don't have any overlap
        idx.reverse()
        lookup = set(idx)
        idx.extend([i for i in xrange(n) if i not in lookup])

        # Reconstruct answer given perm = word indices in left to right order
        result = [A[idx[0]]]
        for i in xrange(1, len(idx)):
            overlap = overlaps[idx[i-1]][idx[i]]
            result.append(A[idx[i]][overlap:])
        return "".join(result)

    # DFS: TLE
    def shortestSuperstring_dfs(self, A):
        def dfs(cur, avail, prev):
            if not avail:
                if len(cur) < self.length:
                    self.ans = cur
                    self.length = len(cur)
                return

            for i in avail:
                cur2 = cur + (A[i][overlap[prev][i]:] if prev is not None else A[i])
                navail = list(avail)
                navail.remove(i)
                dfs(cur2, navail, i)

        import itertools
        n = len(A)
        overlap = [[0] * n for _ in xrange(n)]
        for i, j in itertools.permutations(xrange(n), 2):
            x, y = A[i], A[j]
            for l in reversed(xrange(min(len(x), len(y)) + 1)):
                if x.endswith(y[:l]):
                    overlap[i][j] = l
                    break

        self.ans, self.length = '', float('inf')
        dfs('', range(n), None)
        return self.ans


print(Solution().shortestSuperstring(["alex","loves","leetcode"])) # "alexlovesleetcode"
print(Solution().shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"])) # "gctaagttcatgcatc"
