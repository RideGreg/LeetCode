# Time:  O(1)
# Space: O(1)

# 600
# Given a positive integer n, find the number of non-negative integers less than
# or equal to n, whose binary representations do NOT contain consecutive ones.
#
# Example 1:
# Input: 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
# Note: 1 <= n <= 10^9


# DP 参考：http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
# Let zero[i] be # of binary strings of length i which do not contain any two consecutive 1’s and start (end also ok)
# in 0. Similarly, let one[i] be # of such strings which start (or end) in 1. We can append either 0 or 1 to a string
# ending in 0, but we can only append 0 to a string ending in 1. So
#     zero[i] = zero[i - 1] + one[i - 1]
#     one[i] = zero[i - 1]
# The base cases of above recurrence are zero[1] = one[1] = 1. All the # of strings of length i is just
# zero[i]+one[i]. We can observe that the count is actually (n+2)’th Fibonacci number for n >= 1.
#
# Now we subtract the solutions which is larger than num, we iterate from the MSB to LSB of num:
# - if both bnum[idx-1] and bnum[idx] are '1', all values larger than num should also start with 'xx11xxx',
#   we know no such values are included in solutions. We can stop.
# - if both bnum[idx-1] and bnum[idx] are '0' like 'xx00xxx', we need to subtract all solutions in the
#   format of 'xx01xxx' which is one[size-idx]
# - if bnum[idx-1] and bnum[idx] are '01' or '10', no larger solutions for bit idx (we are working on idx,
#   bit idx-1 already considered) we should subtract, nor we should stop, so we go further to check smaller bits.

class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        bnum = bin(num)[2:]  # bin(8) = '0b1000'
        size = len(bnum)
        one, zero = [0, 1], [0, 1]
        for x in range(2, size+1):
            zero.append(zero[x-1] + one[x-1])
            one.append(zero[x-1])
        ans = zero[size] + one[size]
        for idx in range(1, size):
            if bnum[idx] == bnum[idx-1] == '1':
                break
            elif bnum[idx] == bnum[idx-1] == '0':
                ans -= one[size-idx]
        return ans

    # 首先构造斐波那契数列dp = [1, 2, 3, 5, 8, 13 ...]
    #
    # 记num的二进制串为bnum，其长度为size
    # 令结果ans = dp[size]
    #
    # 从高位到低位遍历bnum，记当前下标为idx：
    #     若bnum[idx] == bnum[idx - 1] == '1'：
    #         说明出现两个连续的1，退出循环
    #
    #     若bnum[idx] == bnum[idx - 1] == '0':
    #         说明出现连个连续的0，ans 减去 dp[size - idx] - dp[size - idx - 1] （等于dp[size - idx - 2]）
    #         This last sentence is hard to understand
    def findIntegers_bookshadow(self, num):
        dp = [1, 2]
        for x in range(2, 32):
            dp.append(dp[x - 1]+ dp[x - 2])
        bnum = bin(num)[2:]
        size = len(bnum)
        ans = dp[size]
        for idx in range(1, size):
            if bnum[idx] == bnum[idx - 1] == '1':
                break
            if bnum[idx] == bnum[idx - 1] == '0':
                ans -= dp[size - idx] - dp[size - idx - 1]
        return ans

    def findIntegers_kamyu(self, num):
        dp = [1, 2]
        for i in range(2, 32):
            dp.append(dp[i-1] + dp[i-2])

        result, prev_bit = 0, 0
        for i in reversed(range(31)):
            if (num & (1 << i)) != 0:
                result += dp[i] # assume i is 2, add # of integers w/ size <= 2
                if prev_bit == 1:
                    result -= 1
                    break
                prev_bit = 1
            else:
                prev_bit = 0
        return result + 1

print(Solution().findIntegers(5)) # 101 -> 5
print(Solution().findIntegers(7)) # 111 -> 5
print(Solution().findIntegers(8)) # 1000 -> 6
print(Solution().findIntegers(9)) # 1001 -> 7
print(Solution().findIntegers(10)) # 1010 -> 8
print(Solution().findIntegers(11)) # 1011 -> 8
