# Time:  O(nlogn)
# Space: O(n)

# Given two arrays A and B of equal size, the advantage of A with respect to B
# is the number of indices i for which A[i] > B[i].
#
# Return any permutation of A that maximizes its advantage with respect to B.
#
# Example 1:
#
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:
#
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
#
# Note:
# - 1 <= A.length = B.length <= 10000
# - 0 <= A[i] <= 10^9
# - 0 <= B[i] <= 10^9

class Solution(object):
    '''
    Greedy Algorithm:
    If the smallest card a in A beats the smallest card b in B, we should pair them. Because every card in A is larger than b,
    any card we place in front of b will score a point. We should use the weakest card to pair with b as it makes the rest cards in A strictly larger.
    If smallest a cannot beat smallest b, a can't beat any cards and we pair it to largest b.

    We sort the 2 lists and create the assignments for each b. Then use our annotations assigned to reconstruct the answer.
    '''
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        sortedB = sorted(B)

        candidates = {b: [] for b in B} # or use collections.defaultdict; b may duplicate, so cannot use a simple dict
        j, k = 0, -1
        for a in sortedA:
            if a > sortedB[j]:
                candidates[sortedB[j]].append(a)
                j += 1
            else:
                candidates[sortedB[k]].append(a)
                k -= 1
        return [candidates[b].pop() for b in B]

    # TLE for input [8,2,4,4,5,6,6,0,4,7], [0,8,7,4,4,2,8,5,2,0]
    # time complexity n!*n, n is length of A
    def advantageCount_permutation(self, A, B):
        import itertools
        def gen(a):
            if not a:
                yield []
            for i in xrange(len(a)):
                for sub in gen(a[:i]+a[i+1:]):
                    yield [a[i]] + sub

        score, ans = 0, A
#        for P in gen(A): # my own permutations
        for P in itertools.permutations(A):
            cur = sum(p > b for p, b in itertools.izip(P, B))
            if cur > score:
                score, ans = cur, P
                if score == len(A): break

        return ans
