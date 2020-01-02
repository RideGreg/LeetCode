# Time:  O(nlogn)
# Space: O(n)

# 1090 weekly contest 141 6/15/19
#
# We have a set of items: the i-th item has value values[i] and label labels[i].
#
# Then, we choose a subset S of these items, such that:
# |S| <= num_wanted
# For every label L, the number of items in S with label L is <= use_limit.
#
# Return the largest possible sum of the subset S.

# 1 <= values.length == labels.length <= 20000
# 0 <= values[i], labels[i] <= 20000
# 1 <= num_wanted, use_limit <= values.length

# greedy
import collections


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        valueLabels = sorted(zip(values, labels), reverse=True)
        counts = collections.defaultdict(int)
        ans = 0
        for v, l in valueLabels:
            if counts[l] < use_limit:
                ans += v
                counts[l] += 1
                num_wanted -= 1
                if num_wanted == 0:
                    break
        return ans

print(Solution().largestValsFromLabels([5,4,3,2,1], [1,1,2,2,3], 3, 1)) # 9
print(Solution().largestValsFromLabels([5,4,3,2,1], [1,3,3,3,2], 3, 2)) # 12
print(Solution().largestValsFromLabels([9,8,8,7,6], [0,0,0,1,1], 3, 1)) # 16
print(Solution().largestValsFromLabels([9,8,8,7,6], [0,0,0,1,1], 3, 2)) # 24
