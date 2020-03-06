# Time:  O(n)
# Space: O(n)

# 1340 weekly contest 174 2/1/2020

# Given an array of integers arr and an integer d. In one step you can jump from index i to index:
#   i + x where: i + x < arr.length and 0 < x <= d.
#   i - x where: i - x >= 0 and 0 < x <= d.
# In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k]
# for all indices k between i and j (More formally min(i, j) < k < max(i, j)).
#
# You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.
#
# Notice that you can not jump outside of the array at any time.

# Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# Output: 4
'''
    --    __
                    --
            __  --
        --    __
--    --          --
  --
0 1 2 3 4 5 6 7 8 9 10
start at index 10. You can jump 10 --> 8 --> 6 --> 7
'''

# https://mp.weixin.qq.com/s/kEQ00_WLqDTG6tbsjQ2Xjw 4 solutions from lee215

try:
    xrange
except NameError:
    xrange = range
import collections
import itertools


# sliding window + top-down dp
# Time O(n), Space O(n). For each step A[i], only check next lower step on its left and right.
class Solution1(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        def dp(i):
            if lookup[i]:
                return lookup[i]
            lookup[i] = 1
            for j in itertools.chain(left[i], right[i]):
                # each dp[j] will be visited at most twice 
                lookup[i] = max(lookup[i], dp(j)+1)
            return lookup[i]

        left, decreasing_dq = [[] for _ in xrange(len(arr))], collections.deque()
        for i in xrange(len(arr)):
            if decreasing_dq and i - decreasing_dq[0] == d+1:
                decreasing_dq.popleft()
            while decreasing_dq and arr[decreasing_dq[-1]] < arr[i]:
                if left[i] and arr[left[i][-1]] != arr[decreasing_dq[-1]]:
                    left[i] = [] #left array中只存左边的next lower steps (may be multiple)
                left[i].append(decreasing_dq.pop()) # dq中位于i左边且数值低于i的index不再需要
            decreasing_dq.append(i)
        right, decreasing_dq = [[] for _ in xrange(len(arr))], collections.deque()
        for i in reversed(xrange(len(arr))):
            if decreasing_dq and decreasing_dq[0] - i == d+1:
                decreasing_dq.popleft()
            while decreasing_dq and arr[decreasing_dq[-1]] < arr[i]:
                if right[i] and arr[right[i][-1]] != arr[decreasing_dq[-1]]:
                    right[i] = []
                right[i].append(decreasing_dq.pop())
            decreasing_dq.append(i)
        # left = [[],[],[0],[],[3],[4],[],[],[6],[],[8]]
        # right = [[1],[],[4],[],[],[6],[7],[],[9],[],[]]

        lookup = [0]*len(arr) # 0 means this index not visited before
        return max(map(dp, xrange(len(arr))))

        # Time O(nd), Space O(n). For each step A[i], check all A[j] on its left and right,
        # until it meet the bound or meet the bigger step.
        """
        def dp(i):
            if not lookup[i]:
                lookup[i] = 1
                for di in [-1, 1]:
                    for j in range(i+di, i+d*di+di, di):
                        if not (0 <= j < n and arr[j] < arr[i]): break
                        lookup[i] = max(lookup[i], dp(j)+1)
            return lookup[i]

        n = len(arr)
        lookup = [0] * n
        return max(map(dp, range(n)))
        """



# Time:  O(nlogn+n)
# Space: O(n)
# mono stack + bottom-up dp
# We can only jump lower, so we sort A[i] do the dp starting from the smallest.
# For each A[i], we only check the next lower step on the left and right.
class Solution(object): # USE THIS
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        left, decreasing_stk = [[] for _ in xrange(len(arr))], []
        for i in xrange(len(arr)):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if i - decreasing_stk[-1] <= d:
                    ''' KENG: wrong, there may be mult index with same value and can be next lower steps.
                    left[i] = [decreasing_stk[-1]]
                    '''
                    if left[i] and arr[left[i][-1]] != arr[decreasing_stk[-1]]:
                        left[i] = [] #left array中只存左边的next lower steps (may be multiple)
                    left[i].append(decreasing_stk[-1])
                decreasing_stk.pop() # stack中位于i左边且数值低于i的index不再需要
            decreasing_stk.append(i)
        right, decreasing_stk = [[] for _ in xrange(len(arr))], []
        for i in reversed(xrange(len(arr))):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if decreasing_stk[-1] - i <= d:
                    # right[i] = [decreasing_stk[-1]]
                    if right[i] and arr[right[i][-1]] != arr[decreasing_stk[-1]]:
                        right[i] = []
                    right[i].append(decreasing_stk[-1])
                decreasing_stk.pop()
            decreasing_stk.append(i)
        # left = [[],[],[0],[],[3],[4],[],[],[6],[],[8]]
        # right = [[1],[],[4],[],[],[6],[7],[],[9],[],[]]

        dp = [1]*len(arr)
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            for j in itertools.chain(left[i], right[i]):
                # each dp[j] will be visited at most twice 
                dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


# Template:
# https://github.com/kamyu104/FacebookHackerCup-2018/blob/master/Final%20Round/the_claw.py
class SegmentTree(object):
    def __init__(self, N,
                 build_fn=lambda x, y: [y]*(2*x),
                 query_fn=max,
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

        result = self.default_val
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
# mono stack + bottom-up dp + segment tree
class Solution3(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        left, decreasing_stk = range(len(arr)), []
        for i in xrange(len(arr)):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if i - decreasing_stk[-1] <= d:
                    left[i] = decreasing_stk[-1]
                decreasing_stk.pop()
            decreasing_stk.append(i)
        right, decreasing_stk = range(len(arr)), []
        for i in reversed(xrange(len(arr))):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if decreasing_stk[-1] - i <= d:
                    right[i] = decreasing_stk[-1]
                decreasing_stk.pop()
            decreasing_stk.append(i)

        segment_tree = SegmentTree(len(arr))
        for _, i in sorted([x, i] for i, x in enumerate(arr)):
            segment_tree.update(i, i, segment_tree.query(left[i], right[i]) + 1)
        return segment_tree.query(0, len(arr)-1)

print(Solution().maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2)) # 4
print(Solution().maxJumps([3,3,3,3,3], 3)) # 1
print(Solution().maxJumps([7,6,5,4,3,2,1], 1)) # 7
print(Solution().maxJumps([7,1,7,1,7,1], 2)) # 2
print(Solution().maxJumps([66], 1)) # 1
print(Solution().maxJumps([
    39,1,1,19,40,34,87,44,30,3,89,55,81,97,84,52,10,8,96,69,17,48,93,84,10,48,1,93,65,
    24,100,26,24,33,52,17,15,26,8,87,69,47,61,58,78,52,2,72,23,9,3,27,36,38,88,20,21,
    79,5,67,22,24,39,7,17,29,3,97,36,51,91,53,98,48,83,52,14,71,91,46,42,88,44,52,74,
    8,39,11,48,59,98,34,43,94,46,20,26,62,6,36,59,77,23,93,6,93,64,18,33,69,56,48,54,
    98,98,53,14,97,47,50,33,87,10,51,92,1,14,27,19,34,83,65,48,44,82,51,81,83,23,8,63,
    70,76,83,46,84,20,7,37,4,69,63,84,71,91,78,58,25,63,85,98,78,21],
62)) # 13