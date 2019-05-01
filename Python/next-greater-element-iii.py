# Time:  O(logn) = O(1)
# Space: O(logn) = O(1)

# 556
# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer
# which has exactly the same digits existing in the integer n and is greater in value than n.
# If no such positive 32-bit integer exists, you need to return -1.
#
# Example 1:
# Input: 12
# Output: 21
# Example 2:
# Input: 21
# Output: -1

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

# 0x7fffffff == 1<<31 - 1 == 2**31 - 1

class Solution(object):
    def nextGreaterElement(self, n): # USE THIS
        """
        :type n: int
        :rtype: int
        """
        A = list(map(int, str(n)))
        pivot = len(A) - 2
        while pivot >= 0 and A[pivot] >= A[pivot+1]:
            pivot -= 1

        if pivot == -1:
            return -1

        i = pivot + 1
        while i < len(A) and A[i] > A[pivot]:
            i += 1

        A[pivot], A[i-1] = A[i-1], A[pivot]
        A[pivot + 1:] = reversed(A[pivot+1:])
        result = int("".join(map(str, A)))
        return -1 if result >= 0x7FFFFFFF else result

    # Do not use this, just for a lessen:
    # 1. actually no need to bisect the digits right to pivot - it has to be a monotonic decreasing list!!
    # 2. CAREFUL to use bisect for 2-item entry, the 2nd item may affect sorting!!
    # 3. CAREFUL to use enumerate on a modified list, the index may not be expected!!
    def nextGreaterElement_bisect(self, n: int) -> int:
        import bisect
        A = list(map(int, str(n)))
        stk = []
        # KENG: very careful using enumerate on a mofified list, the index is not original
        #for i, v in enumerate(reversed(A)):
        for i in reversed(range(len(A))):
            p = bisect.bisect(stk, (A[i], -i))  # insert (A[i], i) will sort incorrectly for same values, different index
            if p < len(stk):
                j = -stk[p][1]
                A[i], A[j] = A[j], A[i]
                A[i + 1:] = sorted(A[i + 1:])   # actually it was sorted, just need reverse
                ans = int(''.join(map(str, A)))
                return ans if ans < (1 << 31) else -1
            bisect.insort(stk, (A[i], -i))
        return -1

print(Solution().nextGreaterElement(1675)) # 1756
print(Solution().nextGreaterElement(1475)) # 1745
print(Solution().nextGreaterElement(11)) # -1
print(Solution().nextGreaterElement(101)) # 110
