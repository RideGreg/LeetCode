# Time:  O(n)
# Space: O(n)

# 1207
# Given an array of integers arr, write a function that returns true if and only if the number of
# occurrences of each value in the array is unique.

import collections


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = collections.Counter(arr)
        lookup = set()
        for v in count.values():
            if v in lookup:
                return False
            lookup.add(v)
        return True


# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = collections.Counter(arr)
        return len(count) == len(set(count.values()))

print(Solution().uniqueOccurrences([1,2,2,1,1,3])) # true
print(Solution().uniqueOccurrences([1,2])) # false
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # true
