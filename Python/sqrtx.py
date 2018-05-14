# Time:  O(logn)
# Space: O(1)

# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
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

    def mySqrt_ming(self, x):
        if x<2: return x
        l,r = 1,x/2
        while l<=r:
            m=(r-l)/2+l
            if m>x/m:
                r = m-1
            elif x/(m+1)>=(m+1):
                l = m+1
            else:
                return m

if __name__ == "__main__":
    print Solution().mySqrt(10)

