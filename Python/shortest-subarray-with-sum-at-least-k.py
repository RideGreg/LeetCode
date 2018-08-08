# Time:  O(n)
# Space: O(n)

# Return the length of the shortest, non-empty,
# contiguous subarray of A with sum at least K.
# If there is no non-empty subarray with sum at least K, return -1.
#
# Example 1:
#
# Input: A = [1], K = 1
# Output: 1
# Example 2:
#
# Input: A = [1,2], K = 4
# Output: -1
# Example 3:
#
# Input: A = [2,-1,2], K = 3
# Output: 3
#
# Note:
# - 1 <= A.length <= 50000
# - -10 ^ 5 <= A[i] <= 10 ^ 5
# - 1 <= K <= 10 ^ 9
'''
Intuition
We can rephrase this as a problem about the prefix sums of A. Let P[i] = A[0] + A[1] + ... + A[i-1].
We want the smallest y-x such that y > x and P[y] - P[x] >= K.

Motivated by that equation, let opt(y) be the largest x such that P[x] <= P[y] - K. We need two key observations:
- If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1, as if x1 satisfies, x2 is always a better answer.
  This implies that all candidates x for opt(y) w/ a given y will have increasing values of P[x].
- If opt(y1) = x, then we do not need to consider this x again. For if we find some y2 > y1 with opt(y2) = x,
  then it represents an answer of y2 - x which is worse (larger) than y1 - x.

Algorithm
Maintain a "monoqueue" of indices of P: a deque of indices x_0, x_1, ... such that P[x_0], P[x_1], ... is increasing.
When adding a new index y to the monoqueue, we'll pop all x_i from the end of the deque where P[x_i] >= P[y]
so that P[x_0], P[x_1], ..., P[y] will be increasing.
If P[y] >= P[x_0] + K, then we don't need to consider x_0 again, and we can pop it from the front of the deque.
'''
try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

import collections


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = len(A)+1 # init to an impossible value
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            while monoq and Py <= P[monoq[-1]]:
                # y is better answer than monoq[-1]. Want opt(y) = largest x with Px <= Py - K
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < len(A)+1 else -1

''' # time: O(n^2) worst case, space: O(n)
    def shortestSubarray_TLE(self, A, K):
        sums = [0]
        for a in A:
            sums.append(sums[-1] + a)

        for d in xrange(1, len(A) + 1):
            for i in xrange(len(sums) - d):
                if sums[i + d] - sums[i] >= K:
                    return d
        return -1
'''

print Solution().shortestSubarray([17,85,93,-45,-21], 150)  #2
print Solution().shortestSubarray([2,-1,2], 3)  #3
print Solution().shortestSubarray([1,2], 4)  #-1