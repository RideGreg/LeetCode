# Time:  O(n)
# Space: O(1)
# a ^ b = (a & !b) || (!a & b)
#       a's 1 + b's 0  a's 0 + b's 1
# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
import collections


class Solution(object):   # USE THIS
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two = 0, 0
        for x in A:
            # if x is 0: one/two stay unchanged. e.g. only when one already True, one stays True (same for two);
            # if x is 1: only when both one and two False, set one True as a fresh one; only when one is True, set two True.
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
        return one

class Solution2(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two, three = 0, 0, 0  # whether this bit has seen one/two/three 1s
        for x in A:
            two |= one & x         # if both one and x are True, or two already True, set two is True
            one ^= x               # first 1 sets one True, second 1 sets one False, so when third 1 comes, three can be true
            three = one & two      # iff both one and two are True
            one &= ~three          # Reset one False iff three is True, otherwise no change
            two &= ~three          # Reset two False iff three is True, otherwise no change
        return one


class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (collections.Counter(list(set(nums)) * 3) - collections.Counter(nums)).keys()[0]


class Solution4(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) / 2


#  every element appears 4 times except for one with 2 times
class SolutionEX(object):
    # @param A, a list of integer
    # @return an integer
    # [1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
    # one/two/three means whether this bit has seen one/two/three 1s,
    # if x is 0: one/two/three stay unchanged.
    # if x is 1: only when one/two/three all False, set one True as a fresh one; only when one is True, set two True;
    # only when two is True, set three True.
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            one, two, three = (~x & one) | (x & ~one & ~two & ~three), (~x & two) | (x & one), (~x & three) | (x & two)
        return two

if __name__ == "__main__":
    print SolutionEX().singleNumber([1,1,1,0,1,0])
    print Solution2().singleNumber([1, 1, 0, 1])
    print Solution().singleNumber([1, 1, 1, 2, 2, 2, 3])
