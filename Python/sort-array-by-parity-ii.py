# Time:  O(n)
# Space: O(1)

# 922
# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.

# Can you do it in place?

# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

# Example 1:
# Input: [4,2,5,7]
# Output: [4,5,2,7]


# Solution: modify in place
# If all even elems are in correct places, all odd items should too. So maintain two pointers on even and odd index separately.

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = 1
        for even in xrange(0, len(A), 2):
            if A[even] % 2:
                while A[odd] % 2:
                    odd += 2
                A[even], A[odd] = A[odd], A[even]
        return A

    def sortArrayByParityII_similar(self, A):
        n, e, o = len(A), 0, 1
        while e < n and o < n:
            if A[e]%2 == 1 and A[o]%2 == 0:
                A[e], A[o] = A[o], A[e]
            if A[e] % 2 == 0:
                e += 2
            if A[o] % 2 == 1:
                o += 2
        return A

    def sortArrayByParityII_tooManyWhile(self, A):
        n, e, o = len(A), 0, 1
        while e < n and o < n:
            while e < n and A[e] % 2 == 0:
                e += 2
            while o < n and A[o] % 2 == 1:
                o += 2
            if e < n and o < n:
                A[e], A[o] = A[o], A[e]
                e += 2
                o += 2
        return A

    # Use stack, WORSE space. We can stop when find 1st even/odd items out of place, not need to put all in stack.
    def sortArrayByParityII_stack(self, A):
        oddToMove, evenToMove = [], []
        for i in xrange(len(A)):
            if i&1 and A[i]&1 == 0:
                if evenToMove:
                    j = evenToMove.pop()
                    A[i], A[j] = A[j], A[i]
                else:
                    oddToMove.append(i)
            elif i&1 == 0 and A[i]&1:
                if oddToMove:
                    j = oddToMove.pop()
                    A[i], A[j] = A[j], A[i]
                else:
                    evenToMove.append(i)
        return A