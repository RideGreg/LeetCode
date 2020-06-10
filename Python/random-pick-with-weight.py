# Time:  ctor: O(n)
#        pickIndex: O(logn)
# Space: O(n)

# 528
# Given an array w of positive integers,
# where w[i] describes the weight of index i,
# write a function pickIndex which randomly picks an index in proportion to its weight.
#
# Note:
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:
#
# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:
#
# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array w. pickIndex has no arguments.
# Arguments are always wrapped with a list, even if there aren't any.
    
import random
import bisect
from typing import List

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]

        1. Convert PDF (Probability Density Function) to CDF (Cumulative Density Function).
           e.g. [2,4,1,3] => [2,6,7,10]
        2. Uniformly sample a value s in [1, sum(weights)].
        3. Use binary search to find first index such that PDF[index] >= s.
           e.g. [1,2] => 0, [3,4,5,6] => 1, [7] => 2, [8,9,10] => 3
        """
        self.__prefix_sum = list(w)
        for i in range(1, len(w)):
            self.__prefix_sum[i] += self.__prefix_sum[i-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1, self.__prefix_sum[-1])
        return bisect.bisect_left(self.__prefix_sum, target)


class Solution_TLE:
    def __init__(self, w: List[int]):
        self.seq = []
        for k, v in enumerate(w):
            self.seq.extend([k] * v) # too long

    def pickIndex(self) -> int:
        return random.choice(self.seq) # pick one from sequence O(sum(w_i)) where 0<=i<n

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
