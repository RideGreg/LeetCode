# Time:  O(n^2), n is the number of disctinct A[i]
# Space: O(n)

# 923
# Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
# As the answer can be very large, return it modulo 10^9 + 7.
# 3 <= A.length <= 3000
# 0 <= A[i] <= 100
# 0 <= target <= 300

# Example 1:
# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20

# Explanation: Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.

# Example 2:
# Input: A = [1,1,2,2,2,2], target = 5
# Output: 12

# Explanation: A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.

# Solution: use Counter for sure, because there may be a lot duplicates, very inefficient to traverse them one by one.
# This problem requires choosing different triples, different with problem 982 "Triples with Bitwise AND Equal To Zero"

import collections
import itertools


class Solution(object):
    # LeetCodeOfficial: Adapt from regular 3sum
    def threeSumMulti(self, A, target): # USE THIS
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)

        ans = 0

        # Now, let's do a 3sum on "keys", for i <= j <= k.
        # We will use count to add the correct contribution to ans.
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1      # j could equals to i
            while j <= k:                # k could equals to j
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) / 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) / 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6

                    j += 1
                    k -= 1
        return ans % MOD


    def threeSumMulti_kamyu(self, A, target):
        count = collections.Counter(A)
        result = 0
        for i, j in itertools.combinations_with_replacement(count, 2): # not easy to come to mind
            k = target - i - j
            if i == j == k:
                result += count[i] * (count[i]-1) * (count[i]-2) // 6  # Combination C(n, 3)
            elif i == j != k:
                result += count[i] * (count[i]-1) // 2 * count[k]

            # eliminate duplicate (i,j,k). i and j may be same or different. Pair (i, j) already clear of duplicate
            # as we have no (j, i), since it's from combinations_with_replacement
            elif max(i, j) < k:
                result += count[i] * count[j] * count[k]
        return result % (10**9 + 7)

    # Ming did in contest, similar idea.
    def threeSumMulti_ming(self, A, target):
        c, ans = collections.Counter(A), 0
        nums = sorted(c)    # equivalent to sorting by keys

        for i in xrange(len(nums)):
            num = nums[i]
            cnt = c[nums[i]]
            if 3*num == target: # not need v>=3
                ans += (cnt*(cnt-1)*(cnt-2)/6)
                ans %= 10**9 + 7
            elif target-2*num in c: # not need v >= 2
                ans += cnt*(cnt-1)/2 * c[target-2*num]
                ans %= 10**9 + 7

            # three different nums, then the problem is regular 3sum with uniqueness
            if i < len(nums) - 2:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if num + nums[j] + nums[k] < target:
                        j += 1
                    elif num + nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        ans += (cnt * c[nums[j]] * c[nums[k]])
                        ans %= 10**9 + 7
                        j, k = j + 1, k - 1
        return ans

print(Solution().threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8)) # 20