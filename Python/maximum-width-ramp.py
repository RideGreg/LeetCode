# Time:  O(n)
# Space: O(n)

# 962
# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp
# is j - i. Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

class Solution(object):
    def maxWidthRamp_stk(self, A): # Descending Stack
        """
        :type A: List[int]
        :rtype: int
        """
        # 0 is the smallest possible i, but elem after it and less than it are also useful.
        # Potential i's: use a stack to store the descending slope (elem larger than previous elems are unuseful.
        # Potential j's: traverse from the end, each i is only used once for rightmost j (reducing complexity),
        # update the answer along the way.
        result = 0
        s = []
        for i in xrange(len(A)):
            if not s or A[s[-1]] > A[i]:
                s.append(i)
        for j in reversed(xrange(len(A))):
            while s and A[s[-1]] <= A[j]:
                result = max(result, j-s.pop())
        return result

    def maxWidthRamp(self, A):
        # caterpillar algorithm: head advances first, then tail.
        n = len(A)
        maxFromLast = [A[-1]] * n
        for i in xrange(n-2, -1, -1):
            maxFromLast[i] = max(maxFromLast[i+1], A[i])

        # tail = i, head = j
        tail, head, ans = 0, 0, 0
        while head < n:
            if tail < head and A[tail] <= A[head]:
                ans = max(ans, head-tail)

            # try advance head as possible; if impossible, advance tail
            if head < n-1 and maxFromLast[head+1]>=A[tail]:
                head += 1
            else:
                tail += 1
                head = max(head, tail)
        return ans

print(Solution().maxWidthRamp([6,5,10,1])) # 2
print(Solution().maxWidthRamp([6,0,8,2,1,5])) # 4
print(Solution().maxWidthRamp([9,8,1,0,1,9,4,0,4,1])) # 7
