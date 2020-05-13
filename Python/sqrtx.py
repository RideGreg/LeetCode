# Time:  O(logn)
# Space: O(1)

# 69
# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x): # USE THIS: find max y where y**2 <= x
        """
        :type x: int
        :rtype: int
        """
        if x < 2: return x
        l, r = 1, x//2
        while l < r:
            m = (r-l+1) // 2 + l
            if m*m <= x: # m is ok
                l = m
            else:
                r = m-1
        return l

    def mySqrt_kamyu(self, x):
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1


if __name__ == "__main__":
    print Solution().mySqrt(10)

