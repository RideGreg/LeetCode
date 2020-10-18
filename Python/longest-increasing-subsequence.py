# Time:  O(nlogn)
# Space: O(n)

# 300
# Given an unsorted array of integers,
# find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4. Note that there may be more
# than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#

# Binary search solution 贪心 + 二分查找：维护一个数组 LIS_tail，储存最长上升子序列的末尾元素的最小值。因为上升子序列的
# 单调性，可用二分查找优化每一步。理念来源于贪心算法：要使上升子序列尽可能的长，需要让序列上升得尽可能慢。

# LIS[i] stores the smallest tail of LIS with length i+1 : when new elem is larger than all elems in LIS,
# append to the end of LIS; otherwise replace the first LIS elem which is larger than it.
# e.g. given [10, 9, 2, 5, 3, 7, 101, 18],
# [10] -> [9] -> [2] -> [2,5] -> [2,3] -> [2,3,7] -> [2,3,7,101] -> [2,3,7,18]

# given [20, 21, 22, 1, 2, 3, 4]:
# [20] -> [20, 21] -> [20,21,22] -> [1,21,22] -> [1,2,22] -> [1,2,3] -> [1,2,3,4]
#                                   ^ this is not a valid subsequence but the length are correct.
#                1 is smallest tail of length-1 LIS, 21 is tail of length-2 LIS, 22 is tail of length-3 LIS.
# the method in this geeksforgeeks article is similar but not straightforward https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        LIS_tail = []
        for n in nums:
            pos = bisect.bisect_left(LIS_tail, n) # Find the first pos satisfying seq[pos] >= target. bisect_right is wrong for [2,2] -> 2
                                                  # because we ask strict increasing subseq, bisect_right appending same value at the end is wrong.
                                                  # bisect works on empty array.
            if pos == len(LIS_tail):
                LIS_tail.append(n)
            else:
                LIS_tail[pos] = n
        return len(LIS_tail)


# Range Maximum Query
class SegmentTree(object):  # 0-based index
    def __init__(self, N,
                 build_fn=lambda x, y: [y]*(2*x),
                 query_fn=lambda x, y: y if x is None else max(x, y),  # (lambda x, y: y if x is None else min(x, y))
                 update_fn=lambda x, y: y,
                 default_val=0):
        self.N = N
        self.H = (N-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.default_val = default_val
        self.tree = build_fn(N, default_val)
        self.lazy = [None]*N

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def update(self, L, R, h):  # Time: O(logN), Space: O(N)
        def pull(x):
            while x > 1:
                x //= 2
                self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])
                if self.lazy[x] is not None:
                    self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:  # is right child
                self.__apply(L, h) 
                L += 1
            if R & 1 == 0:  # is left child
                self.__apply(R, h)
                R -= 1
            L //= 2
            R //= 2
        pull(L0)
        pull(R0)

    def query(self, L, R):  # Time: O(logN), Space: O(N)
        def push(x):
            n = 2**self.H
            while n != 1:
                y = x // n
                if self.lazy[y] is not None:
                    self.__apply(y*2, self.lazy[y])
                    self.__apply(y*2 + 1, self.lazy[y])
                    self.lazy[y] = None
                n //= 2

        result = None
        if L > R:
            return result

        L += self.N
        R += self.N
        push(L)
        push(R)
        while L <= R:
            if L & 1:  # is right child
                result = self.query_fn(result, self.tree[L])
                L += 1
            if R & 1 == 0:  # is left child
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result
    
    def __str__(self):
        showList = []
        for i in xrange(self.N):
            showList.append(self.query(i, i))
        return ",".join(map(str, showList))


# Time:  O(nlogn)
# Space: O(n)
# optimized from Solution4
class Solution3(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(set(nums))
        lookup = {num:i for i, num in enumerate(sorted_nums)}
        segment_tree = SegmentTree(len(lookup))
        for i in xrange(len(nums)):
            segment_tree.update(lookup[nums[i]], lookup[nums[i]],
                                (segment_tree.query(0, lookup[nums[i]]-1) if lookup[nums[i]] >= 1 else 0) + 1)
        return segment_tree.query(0, len(lookup)-1) if len(lookup) >= 1 else 0


# Time:  O(n^2)
# Space: O(n)
# Traditional DP solution.
class Solution4(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

print(Solution().lengthOfLIS([2,3,4,1]))
