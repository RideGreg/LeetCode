# Time:  O(n)
# Space: O(1)

# 801
# We have two integer sequences A and B of the same non-zero length.
#
# We are allowed to swap elements A[i] and B[i].
# Note that both elements are in the same index position in their respective sequences.
#
# At the end of some number of swaps, A and B are both strictly increasing.
# (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)
#
# Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
# It is guaranteed that the given input always makes it possible.
#
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation:
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.
#
# Note:
# - A, B are arrays with the same length, and that length will be in the range [1, 1000].
# - A[i], B[i] are integer values in the range [0, 2000].

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int

        Dynamic Programming
        Intuition
        The cost of making both sequences increasing up to the first i columns can be expressed in terms of the cost of
        making both sequences increasing up to the first i-1 columns. Because the only thing that matters to the ith column
        is whether the previous column was swapped or not. This makes dynamic programming an ideal choice.

        Let's remember n1 (natural1), the cost of making the first i-1 columns increasing and not swapping the i-1th column;
        and s1 (swapped1), the cost of making the first i-1 columns increasing and swapping the i-1th column.

        Now we want candidates n2 and s2. There are three possibilities: 1. A[i] must stay with A[i-1], B[i] must stay with
        B[i-1], i.e. swap both or none; 2. A[i] must stay w/ B[i-1], B[i] must stay w/ A[i-1], i.e. must swap 1 and only 1 column;
        3. A[i]/B[i] can stay w/ either A[i-1] or B[i-1], i.e. use min value from last column.

        In fact, n1/s1 and n2/s2 can use the same pair of vars.
        """
        n, s = 0, 1
        for i in range(1, len(A)):
            if A[i] <= B[i-1] or B[i] <= A[i-1]: # must swap both columns or no swap
                n, s = n, s + 1
            elif A[i] <= A[i-1] or B[i] <= B[i-1]: # must swap 1 column
                n, s = s, n + 1
            else: # can swap or not
                n, s = min(n, s), min(n, s) + 1
        return min(n, s)
