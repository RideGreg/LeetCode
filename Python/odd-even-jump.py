# Time:  O(nlogn)
# Space: O(n)

# 975
# You are given an integer array A.  From some starting index, you can make a series of jumps.
# The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the
# (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.
#
# You may from index i jump forward to index j (with i < j) in the following way:
#
# During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that
# A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j,
# you can only jump to the smallest such index j.
# During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that
# A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j,
# you can only jump to the smallest such index j.
# (It may be the case that for some index i, there are no legal jumps.)

# A starting index is good if, starting from that index, you can reach the end of the array
# (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)
#
# Return the number of good starting indexes.


# Solution: Monotonic Stack
# Intuition
#
# First, where you jump to is determined only by the state of (your current index and the jump number parity).
#
# For each state, there is exactly one state you could jump to (or you can't jump.) If we somehow knew these jumps,
# we could solve the problem by a simple traversal.
#
# So the problem reduces to solving this question: for index i during an odd numbered jump, what index do we jump to
# (if any)? The question for even-numbered jumps is similar.
#
# Algorithm
#
# Let's figure out where index i jumps to, assuming this is an odd-numbered jump.
#
# Let's order A from smallest to largest. When we encouter a value A[j] = v, we cannot determine which index it jumps to
# because it would scan forward O(n^2). Instead, we can determine which indices jump to it. We check the values
# that we have already processed (which are <= v) but haven't find jump-to index.
#
# Naively this is a little slow, but we can speed this up with a common trick for harder problems: a monotonic stack.
# (For another example of this technique, please see the solution to this problem: (Sum of Subarray Minimums))
#
# Let's store the indices i of the processed values v0 = A[i] in a stack, and maintain the invariant that this is monotone
# decreasing. When we add a new index j, we pop all the smaller indices i < j from the stack, which all jump to j.
#
# Afterwards, we know oddnext[i], the index where i jumps to if this is an odd numbered jump. Similarly, we know evennext[i].
# We can use this information to quickly build out all reachable states using dynamic programming.

class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def findNext(idx):
            result = [None]*len(idx)
            stack = []  # invariant: stack is decreasing
            for i in idx:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        
        idx = sorted(range(len(A)), key = lambda i: A[i])
        next_higher = findNext(idx)
        idx.sort(key = lambda i: -A[i])
        next_lower = findNext(idx)

        odd, even = [False]*len(A), [False]*len(A)
        odd[-1], even[-1] = True, True
        for i in reversed(xrange(len(A)-1)):
            if next_higher[i]:
                odd[i] = even[next_higher[i]]
            if next_lower[i]:
                even[i] = odd[next_lower[i]]
        return sum(odd)

    def oddEvenJumps_bst(self, A):
        import bisect
        N = len(A)
        odd, even = [False] * N, [False] * N
        odd[-1] = even[-1] = True
        visited = [A[-1]]
        v2id = {A[-1]: N - 1}
        for i in xrange(N - 2, -1, -1):
            # find next_higher
            pos = bisect.bisect_left(visited, A[i])
            if pos < len(visited) and even[v2id[visited[pos]]]:
                odd[i] = True

            # find next_lower
            pos = bisect.bisect_right(visited, A[i])
            if pos > 0 and odd[v2id[visited[pos - 1]]]:
                even[i] = True

            bisect.insort(visited, A[i])
            v2id[A[i]] = i
        return sum(odd)

print(Solution().oddEvenJumps([10,13,12,14,15])) # 2
print(Solution().oddEvenJumps([2,3,1,1,4])) # 3
