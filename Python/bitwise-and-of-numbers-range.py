# Time:  O(logn), 时间复杂度取决于 m 和 n 二进制展开的位数
# Space: O(1)

# 201
# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.
#


# 对区间内所有数字执行按位与运算，结果是所有对应二进制字符串的公共前缀再用零补上后面的剩余位。
#  9: 1 0 0 1
# 10: 1 0 1 0
# 11: 1 0 1 1
# 12: 1 1 0 0
# 
# 证明：假设公共前缀为前i位，从第i+1位开始有不同，那么第i+1位的bits一定是
# 0,0...0,1,1...1；而且变化前后的两个数一定为
# xxx01111
# xxx10000
# 所以按位与结果是公共前缀后用零补齐。进一步简化找到m和n的公共前缀后用零补齐即可。
class Solution(object):
    # @param m, an integer
    # @param n, an integer
    # @return an integer

    # Brian Kernighan位移算法，清除二进制串中最右边的 1，直到它小于或等于m，
    # 此时i+1位的1一定被消去了，也即非公共前缀部分的 1均被消去。
    def rangeBitwiseAnd(self, m, n):
        while m < n:
            n &= n - 1
        return n


    # Naive位移算法：
    # 两个数字不断向右移动，直到数字相等，即数字被缩减为它们的公共前缀。然后，
    # 通过将公共前缀向左移动，将零添加到公共前缀的右边以获得最终结果。
    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        shift = 0   
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift


    def rangeBitwiseAnd3(self, m, n):
        i, diff = 0, n-m
        while diff:
            diff >>= 1
            i += 1
        return n & m >> i << i


print(Solution().rangeBitwiseAnd(5, 7)) # 4
print(Solution().rangeBitwiseAnd(0, 1)) # 0