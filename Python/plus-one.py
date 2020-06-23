# Time:  O(n)
# Space: O(1)

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# in-place solution
class Solution(object):
    def plusOne(self, digits): # USE THIS
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            carry, digits[i] = divmod(digits[i]+carry, 10)
            if carry == 0:
                break
        return [1] + digits if carry else digits


    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(xrange(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1 # when a digit is not 9, we can stop here
                return digits
        digits[0] = 1  # all 9s, change to 1000...
        digits.append(0)
        return digits


if __name__ == "__main__":
    print Solution().plusOne([9, 9, 9, 9])
