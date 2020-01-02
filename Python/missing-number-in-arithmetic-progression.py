# Time:  O(logn)
# Space: O(1)

# 1228 biweekly contest 11 10/19/2019
# In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
#
# Then, a value from arr was removed that was not the first or last value in the array.
#
# Return the removed value.

# Constraints:
# 3 <= arr.length <= 1000
# 0 <= arr[i] <= 10^5

class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def invalid(d, x):
            return arr[x] != arr[0] + d*x

        d = (arr[-1]-arr[0])//len(arr)
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right-left)//2
            if invalid(d, mid):
                right = mid  # mid eligible
            else:
                left = mid+1   # mid not eligible
        return arr[0] + d*left


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return (arr[0]+arr[-1])*(len(arr)+1)//2 - sum(arr)

print(Solution().missingNumber([5,7,11,13])) # 9
print(Solution().missingNumber([15,13,12])) # 14
