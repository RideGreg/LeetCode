# Time:  O(n)
# Space: O(1)
# a ^ 0 = a, a ^ a = 0
# a ^ b = (a & !b) || (!a & b)
#       a's 1 is b's 0  a's 0 is b's 1

# 137
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
            #     init, 1st 1 come, 2nd 1 come, 3rd 1 come (reset to 0)
            # One   0     1            0           0
            # Two   0     0            1           0
            # sequential statements
            one = ~two & (one ^ x)  # only set when 1st or 4th shown; for 2nd time, remove as x^x = 0;
                                    # for 3rd time, not set as two is true
            two = ~one & (two ^ x)
            '''
            # concurrent statements
            # if x is 0: one/two stay unchanged.
            # if x is 1: only when both one and two False, set one True as a fresh one; only when one is True, set two True.
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
            '''
        return one

    def singleNumber2(self, A):
        one, two, three = 0, 0, 0  # whether this bit has seen one/two/three 1s
        for x in A:
            two |= one & x         # if both one and x are True, or two already True, set two is True
            one ^= x               # first 1 sets one True, second 1 sets one False, so when third 1 comes, three can be true
            three = one & two      # iff both one and two are True
            one &= ~three          # Reset one False iff three is True, otherwise no change
            two &= ~three          # Reset two False iff three is True, otherwise no change
        return one


    def singleNumber3(self, nums): # use Counter, space O(n)
        return (collections.Counter(list(set(nums)) * 3) - collections.Counter(nums)).keys()[0]

    def singleNumber4(self, nums): # use sum, Space O(n)
        return (sum(set(nums)) * 3 - sum(nums)) / 2


#  every element appears 4 times except for one with 2 times
class SolutionEX(object):
    # @param A, a list of integer
    # @return an integer
    # [1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
    # one/two/three means whether this bit has seen one/two/three 1s.
    #
    #     init, 1st 1 come, 2nd 1 come, 3rd 1 come, 4th 1 come (reset to 0)
    # One   0     1            0           0          0
    # Two   0     0            1           0          0
    # Three 0     0            0           1          0
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            # sequential statements
            one = ~two & ~three & (one ^ x) # only set when 1st or 5th shown; for 2nd time, remove as x^x = 0;
                                            # for 3rd time, not set as two is true; for 4th time not set as three is true
            two = ~one & ~three & (two ^ x)
            three = ~one & ~two & (three ^ x)
            '''
            # concurrent statements
            # if x is 0: one/two/three stay unchanged.
            # if x is 1: only when one/two/three all False, set one True as a fresh one; only when one is True, set two True;
            # only when two is True, set three True.
            one, two, three = (~x & one) | (x & ~one & ~two & ~three), \
                              (~x & two) | (x & one), \
                              (~x & three) | (x & two)
            '''
        return two

if __name__ == "__main__":
    print(SolutionEX().singleNumber([1,1,1,2,1,2])) # 2
    print(Solution().singleNumber([1, 1, 0, 1])) # 0
    print(Solution().singleNumber([1, 1, 1, 2, 2, 2, 3])) # 3
