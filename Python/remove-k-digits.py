# Time:  O(n)
# Space: O(n)

# 402
# Given a non-negative integer num represented as a string,
# remove k digits from the number so that the new number is the smallest possible.
#
# Note:
# The length of num is less than 10^5 and will be >= k.
# The given num does not contain any leading zero.
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200.
# Note that the output must not contain leading zeroes.
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

class Solution(object):
    # greedy with stack
    # 删除规则: cliff的左侧数字。一旦从序列中删除一个数字，剩下数字就形成了一个新问题，不能盲目前进，必须继续使用删除规则。
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k:
            stack = stack[:-k] # stack[:0] is empty '', so need to check k
        return ''.join(stack).lstrip('0') or '0'

    # LTE 暴力法: 列举所有可能的组合，n! grows faster than k^n exponential time complexity
    # 并找出其中最小的数字 (不可将数字字符串转换为数值比较，因为一个无符号的 32 位整数所能容纳的最大值是10位数字
    # （即 4294967295），但很多测试用例是由数百位数字组成的。应该从左到右逐个比较数字序列）。
    #

print(Solution().removeKdigits("1432219", 3)) # '1219'
print(Solution().removeKdigits('10200', 1)) # '200'
print(Solution().removeKdigits('10', 2)) # '0'
print(Solution().removeKdigits('12219', 1)) # '1219'
print(Solution().removeKdigits('12219', 2)) # '119'
print(Solution().removeKdigits('12269', 1)) # '1226'
