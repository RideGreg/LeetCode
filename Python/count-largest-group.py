# Time:  O(nlogn)
# Space: O(n)

# 1399
# Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.
# Return how many groups have the largest size.

import collections


class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """

        def getSum(x):
            ans = 0
            while x:
                x, r = divmod(x, 10)
                ans += r
            return ans

        count = collections.Counter()
        for x in range(1, n+1):
            count[sum(map(int, str(x)))] += 1
            # or count[getSum(x)] += 1
        max_count = max(count.values())
        return sum(v == max_count for v in count.values())

print(Solution().countLargestGroup(13)) # 4
print(Solution().countLargestGroup(2)) # 2
print(Solution().countLargestGroup(15)) # 6
print(Solution().countLargestGroup(24)) # 5