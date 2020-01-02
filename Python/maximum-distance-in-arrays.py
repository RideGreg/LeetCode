# Time:  O(n)
# Space: O(1)

# 624
# Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two
# different arrays (each array picks one) and calculate the distance. We define the distance between two integers
# a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

# The total number of the integers in all the m arrays will be in the range of [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        result, min_val, max_val = 0,  arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            result = max(result, \
                         max(max_val - arrays[i][0], \
                             arrays[i][-1] - min_val))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return result

print(Solution().maxDistance([[1,2,3], [4,5], [1,2,3]])) # 4