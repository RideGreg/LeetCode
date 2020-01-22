# Time:  O(n)
# Space: O(1)

# 1299 biweekly contest 16 12/28/2019

# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
#
# After doing so, return the array.

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        curr_max = -1
        for i in reversed(xrange(len(arr))):
            arr[i], curr_max = curr_max, max(curr_max, arr[i])
        return arr
