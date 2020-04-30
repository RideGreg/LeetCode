# Time:  O(k), where k is the steps to be happy number
# Space: O(k)

# 202
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum
# of the squares of its digits, and repeat the process until
# the number equals 1 (where it will stay), or it loops endlessly
# in a cycle which does not include 1. Those numbers for which
# this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):    # USE THIS
        lookup = set()
        while n != 1 and n not in lookup:
            lookup.add(n)
            n = sum(int(c)**2 for c in str(n))
        return n == 1

    def isHappy2(self, n):
        ht = set()
        while n != 1 and n not in ht:
            ht.add(n)
            m = 0
            while n:
                n, p = divmod(n, 10)
                m += p**2
            n = m
        return n == 1

print(Solution().isHappy(19)) # True