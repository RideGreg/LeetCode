# Time:  O(logn)
# Space: O(1)
# 9
# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string or array, note the restriction of *using extra space*.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow (e.g. 9 at LSB switch to MSB and > INT_MAX).
# How would you handle such case?
#
# There is a more generic way of solving this problem: only revert the 2nd half digits.
#

class Solution:
    # @return a boolean
    def isPalindrome(self, x):         # USE THIS:revert the second half
        if x < 0: return False
        import math
        sz = int(math.log10(x)) + 1
        first, second = divmod(x, 10**(sz//2))
        if sz & 1:
            first //= 10

        second_rev = 0
        while second:
            second_rev = second_rev * 10 + second % 10
            second //= 10
        return first == second_rev

    # compare digits at left, right ends
    def isPalindrome2(self, x):
        if x < 0: return False
        div = 1
        while x / div >= 10:
            div *= 10

        while x:
            left, right = x//div, x%10
            if left != right: return False
            x = (x % div) // 10
            div //= 100
        return True

    def isPalindrome3(self, x): # reverting all digits may overflow
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse = reverse * 10 + copy % 10
            copy //= 10

        return x == reverse

if __name__ == "__main__":
    print(Solution().isPalindrome(12321))
    print(Solution().isPalindrome(12320))
    print(Solution().isPalindrome(-12321))
