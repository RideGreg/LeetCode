class Solution(object):
    def bestRotation(self, A):
        import collections
        d = collections.defaultdict(int)
        maxscore, ans = 0, 0
        for i in xrange(len(A)):
            if A[i] <= i:
                maxscore += 1
                d[A[i] - i] += 1
        score = maxscore
        for K in xrange(1, len(A)):
            if A[K - 1] <= len(A) - 1:
                score += 1
            d[A[K - 1] - (len(A) - 1) - K] += 1
            if 1 - K in d:
                score -= d[1 - K]

            if score > maxscore:
                maxscore = score
                ans = K
        return ans

print Solution().bestRotation([2, 3, 1, 4, 0])
print Solution().bestRotation([1, 3, 0, 2, 4])