# Time:  O(n)
# Space: O(1)

# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
# Return true if and only if the number of global inversions is equal to the number of local inversions.
#
# Example 1:
#
# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
#
# Example 2:
#
# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
#
# Note:
# - A will be a permutation of [0, 1, ..., A.length - 1].
# - A will have length in range [1, 5000].
# - The time limit for this problem has been reduced.

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # All local inversions are global inversions. We cannot have non-local global inv which is
        # A[i]>A[j] with i+2<=j. So number i can only be on index i-1, i, i+1: if i is on an index < i-1,
        # then there must be 2 numbers less than i are behind i's position; similar if i is on an index > i+1.
        return all(abs(v-i) <= 1 for i,v in enumerate(A))

    # FenwickTree: TLE in Python. But good to know how to get global inversion number.
    # https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
    # https://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/
    # FenwickTree key points: 1. physically a list, logically a tree. Each tree node stores the sum of some
    #   items in the input list, in general, sum of the numbers since the item (exclusive) mapping to its parent
    #   in the tree, where parent is found by clearing the lowbit in binary of its index. Think the input list
    #   like a 1-based array: odd-id node stores itself, node w/ id 2^i stores sum of first i number, other node stores
    #   sum of (previous 2^k, itself].
    #   1 (in[1])
    #   2 (in[1]+in[2])
    #   3 (in[3])
    #   4 (in[1]+in[2]+in[4]+in[4])
    #   5 (in[5])
    #   6 (in[5]+in[6])
    #   7 (in[7])
    #   8 (in[1]+in[2]+in[4]+in[4]+in[5]+in[6]+in[7]+in[8])
    #   9 (in[9]) ...
    # 2. when query sum: add values stored in current node and all its ancestors (iteratively clearing lowbit).
    # 3. when update a number in input list: all nodes containing this number (iteratively adding lowbit) should be updated.

    def isIdealPermutation_ft(self, A):
        def localInv(A):
            return sum(A[i] > A[i + 1] for i in xrange(len(A) - 1))

        def globalInv(A):
            ft = FenwickTree(len(A))
            ans = 0
            for a in reversed(A):
                a += 1
                ans += ft.sum(a - 1)
                ft.add(a, 1)
            return ans

        return localInv(A) == globalInv(A)

    # Mergesort: TLE in Python.
    def isIdealPermutation_mergesort(self, A):
        def merge(a, b):
            c, gInv = [], 0
            i, j = 0, 0
            while len(a) != i and len(b) != j:
                if a[i] < b[j]:
                    c.append(a[i])
                    i+=1
                else:
                    c.append(b[j])
                    j+=1
                    gInv += len(a) - i
            if len(a) == i: c += b[j:]
            else: c += a[i:]
            return [c, gInv]

        def mergesort(x):
            if len(x) == 1:
                return [x, 0, 0]
            else:
                middle = len(x) / 2
                l = 1 if x[middle-1]>x[middle] else 0
                [a, g1, l1] = mergesort(x[:middle])
                [b, g2, l2] = mergesort(x[middle:])
                [c, g] = merge(a, b)
                return [c, g+g1+g2, l+l1+l2]

        [c, g, l] = mergesort(A)
        print l, g
        return l==g

class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.nums = [0] * (n+1)

    def lowbit(self, x):
        return x & -x

    def add(self, x, val):
        while x <= self.n:
            self.nums[x] += val
            x += self.lowbit(x)

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.nums[x]
            x -= self.lowbit(x)
        return res

print Solution().isIdealPermutation([0,5,2,3,4,1,6])
print Solution().isIdealPermutation([1,0,2])
print Solution().isIdealPermutation([1,2,0])
