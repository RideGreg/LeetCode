# -*- encoding=utf-8 -*-
# Time:  O(n)
# Space: O(n)

# 907
# Given an array of integers A, find the sum of min(B),
# where B ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1],
#                            [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
#
# Note:
# - 1 <= A.length <= 30000
# - 1 <= A[i] <= 30000


# Prev/Next Array
# Intuition
#
# Instead of finding all subarrays (O(n^2)) and add their min. Let's count the # of subarrays #(j) for which A[j] is the
# right-most minimum (O(n)). The answer will be sum #(j) * A[j]. (We must say right-most so that we form disjoint sets
# of subarrays and do not double count any, as the minimum of an array may not be unique.)
#
# I.e. for each A[j], find the range of [i, k] where A[j] is right-most minimum
#  >=
#   >=      <
#    >=    <
#      A[j]
#
# This in turn brings us the question of knowing the smallest index i <= j for which A[i], A[i+1], ..., A[j] are all >= A[j];
# and the largest index k >= j for which A[j+1], A[j+2], ..., A[k] are all > A[j].
#
# Algorithm
#
# E.g. if A = [10, 3, 4, 5, _3_, 6, 3, 10] and we would like to know #(j = 4) [the count of the second 3, which is marked],
# we would find i = 1 and k = 5. From there, the actual count is #(j) = (j - i + 1) * (k - j + 1).
#
# These queries (ie. determining (i, k) given j) is a classic problem that can be answered with a stack. We actually find
# i-1 (largest index whose number < A[j], and k+1 (smallest index whose number <= A[j].
#
# The idea is to maintain stack. For 'prev' array, the top of stack is index of the previous nearest number < A[j];
# for 'next' array, the top of stack is index of the next nearest number <= A[j].
#
# This is quite difficult to figure out, but this type of technique occurs often in many other problems,
# so it is worth learning in detail.

import itertools


# Ascending stack solution
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        prev, nex = [None]*n, [None]*n
        stk = []
        for i in xrange(n):
            # discard previous numbers >= A[i] to find the nearest number which cannot put in a valid subarray
            while stk and A[stk[-1]] >= A[i]:
                stk.pop()
            prev[i] = stk[-1] if stk else -1
            stk.append(i)
        stk = []
        for i in xrange(n-1,-1,-1):
            while stk and A[stk[-1]] > A[i]:
                stk.pop()
            nex[i] = stk[-1] if stk else n
            stk.append(i)
        return sum(A[i]*(i-prev[i])*(nex[i]-i) for i in xrange(n)) % (10**9+7) # KENG: missing parenthesis, better use a constant

    # not good: stack stores a tuple (index, # of valid items) - complicated
    def sumSubarrayMins_kamyu(self, A):
        M = 10**9 + 7

        left, s1 = [0]*len(A), []
        for i in xrange(len(A)):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])

        right, s2 = [0]*len(A), []
        for i in reversed(xrange(len(A))):
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])

        return sum(a*l*r for a, l, r in itertools.izip(A, left, right)) % M

    def sumSubarrayMins_gerksforgerks(self, A):
        n = len(A)
        stack, nextLow = [], [n]*n
        for i in reversed(xrange(n-1)):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if stack:
                nextLow[i] = stack[-1]
            stack.append(i)

        dp = [0] * (n+1)
        for i in reversed(xrange(n)):
            dp[i] = (nextLow[i]-i) * A[i] + dp[nextLow[i]]
        return sum(dp) % (10**9+7)

# Maintain Stack of Minimums
# Intuition
    #
    # For a specific j, let's try to count the minimum of each subarray [i, j]. The intuition is that as we increment j++,
    # these minimums may be related to each other. Indeed, min(A[i:j+1]) = min(A[i:j], A[j]).
    #
    # Playing with some array like A = [1,7,5,2,4,3,9], with j = 6 the minimum of each subarray [i, j] is B = [1,2,2,2,3,3,9].
    # We can see that there are critical points i = 0, i = 3, i = 5, i = 6 where a minimum is reached for the first time
    # when walking left from j.
    #
    # Algorithm
    #
    # Let's try to maintain an RLE (run length encoding) of these critical points B. More specifically, for the above
    # (A, j), we will maintain stack = [(val=1, count=1), (val=2, count=3), (val=3, count=2), (val=9, count=1)], that
    # represents a run length encoding of the subarray minimums B = [1,2,2,2,3,3,9]. For each j, we want sum(B).
    #
    # As we increment j, we will have to update this stack to include the newest element (val=x, count=1). We need to pop
    # off all values >= x before, as the minimum of the associated subarray [i, j] will now be A[j] instead of what it was before.
    #
    # At the end, the answer is the dot product of this stack:
    #    ∑  e.val∗e.count
    # e ∈ stack
    # ​which we also maintain on the side as the variable dot.

    def sumSubarrayMins_LeetCodeOfficial2(self, A):
        MOD = 10**9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD

print(Solution().sumSubarrayMins([3,1,2,4])) # 17: prev: [-1,-1,1,2], nex: [1,4,4,4]
print(Solution().sumSubarrayMins([48,87,27])) # 264: prev: [-1,0,-1], nex: [2,2,3]
print(Solution().sumSubarrayMins([59,91])) # 209: prev: [-1,0], nex: [2,2]