# Time:  O(n + klogk), n is length of A, k is length of counter.
# Space: O(k)

# 954
# Given an array of integers A with even length, return true if and only if it is possible to reorder it such that
# A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

# Example 1:
# Input: [3,1,3,6]
# Output: false

# Example 2:
# Input: [2,1,2,6]
# Output: false

# Example 3:
# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

# Example 4:
# Input: [1,2,4,16,8,4]
# Output: false

# Greedy
# If x is currently the array element with the least absolute value, it must pair with 2*x,
# as there does not exist any other x/2 to pair with it.

import collections


class Solution(object):

    def canReorderDoubled(self, A): # fast, kamyu: sort counter, reduce count of same key altogether
        """
        :type A: List[int]
        :rtype: bool
        """
        count = collections.Counter(A)
        for x in sorted(count, key=abs):
            if count[x] > count[2*x]:
                return False
            count[2*x] -= count[x]
        return True

    def canReorderDoubled_LeetCodeOfficial(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] > 0:
                if count[2*x] == 0: return False
                count[x] -= 1
                count[2*x] -= 1
        return True

    def canReorderDoubled_mingNaive(self, A):
        cnt = collections.Counter(A)
        for a in sorted(A):
            if cnt[a] > 0:
                if a > 0:
                    if cnt[2*a] <= 0:
                        return False
                    cnt[a] -= 1
                    cnt[2*a] -= 1
                elif a == 0:
                    if cnt[0] < 2: return False
                    cnt[0] -= 2
                else:
                    if a%2 != 0 or cnt[a/2]<=0: return False # must check a%2, otherwise [-3, -5] is okay
                    cnt[a] -= 1
                    cnt[a/2] -= 1
        return True

