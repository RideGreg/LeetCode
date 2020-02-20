# Time:  O(n^2 * logn)
# Space: O(n)

# 1187 weekly contest 153 9/7/2019

# Given two integer arrays arr1 and arr2, return the minimum # of operations (possibly zero) needed to make arr1 strictly increasing.
#
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].
#
# If there is no way to make arr1 strictly increasing, return -1.

# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9

import collections
import bisect

# Similar to binary search solution in longest-increasing-subsequence.py (LIS)
# dp record the tail values we can place at this position, and the cost to get to this state.
# When building next dp for (i+1)-th position, for (i+1)-th element:
# if it's larger than the tail value from i-th state, we have two choices:
#  1, append it so no operation needs to be made.
#  2, choose from arr2 the smallest element that is larger than i-th element and add one operation.
# If it's not larger than the i-th state, we definitely need to try a possible operation.

class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr2 = sorted(set(arr2))
        dp = {0: -1}  # dp[cost] = init_tail_val
        for x in arr1:
            ndp = collections.defaultdict(lambda: float("inf"))
            for cost, tail in dp.items():
                # if x larger than previous tail, get a new state with same cost
                if x > tail:
                    ndp[cost] = min(ndp[cost], x)

                # Instead of appending x, find new tail from arr2 which should be first num which is larger than x.
                # KENG: cannot require arr2[pos] < x, x may be already too small for previous tail
                # eg. [1,5,3,6,7], [1,3,4]
                pos = bisect.bisect_right(arr2, tail)
                if pos < len(arr2):
                    ndp[cost+1] = min(ndp[cost+1], arr2[pos])
            dp = ndp
            if not dp:
                return -1
        return min(dp)

print(Solution().makeArrayIncreasing([1,5,3,6,7], [1,3,2,4])) # 1
# dp: {0:1, 1:1}
# =>  {0:5, 1:2, 2:2}
# =>  {1:3, 2:3, 3:3}
# =>  {1:6, 2:4, 3:4, 4:4}
# =>  {1:7, 2:7, 3:7, 4:7}

print(Solution().makeArrayIncreasing([1,5,3,6,7], [4,3,1])) # 2
print(Solution().makeArrayIncreasing([1,5,3,6,7], [1,6,3,3])) # -1