# Time:  O(n)
# Space: O(1)

# 1089 weekly contest 141 6/15/19
#
# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.

from typing import List

class Solution(object):
    def duplicateZeros(self, arr: List[int]) -> None: # USE THIS
        i, cnt = 0, 0
        for i, x in enumerate(arr): # get i the start point of reading
            cnt += 1 if x else 2
            if cnt >= len(arr):
                break

        w = len(arr) - 1 # start point of writing
        for r in range(i, -1, -1):
            if w == r: break # optimize if remaining are the same
            arr[w] = arr[r]
            w -= 1
            if arr[r] == 0 and (r != i or cnt == len(arr)):
                arr[w] = arr[r]
                w -= 1
        print(arr)
        return

    def duplicateZeros_kamyu(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        shift, i = 0, 0
        while i+shift < len(arr):
            shift += int(arr[i] == 0)
            i += 1
        i -= 1
        while shift:
            if i+shift < len(arr):
                arr[i+shift] = arr[i]
            if arr[i] == 0:
                shift -= 1
                arr[i+shift] = arr[i]
            i -= 1

print((Solution().duplicateZeros([1,0,2,3,0,4,5,0]))) # [1,0,0,2,3,0,0,4]
print((Solution().duplicateZeros([1,2,3]))) # [1,2,3]