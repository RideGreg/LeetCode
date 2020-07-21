# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)

# 307
# Given an integer array nums, find the sum of
# the elements between indices i and j (i <= j), inclusive.
#
# The update(i, val) function modifies nums by
# updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update
# and sumRange function is distributed evenly.

try:
    xrange
except NameError:
    xrange = range

# Binary Indexed Tree (BIT) solution. N-ARY TREE smaller & faster than segment tree.
# https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
# input [2,4,5,7,8,9] will be stored as [0,2,6,5,18,8,17]. Root tree nodes is a dummy node.
#
# Tree structure: each node stores a RANGE of prefix sum.
# If binary representation of i has k training zeros, node i stores a RANGE of 2^k previous numbers.
# Parent node Id equals children node removing Last Set Bit.
# BUT works for sum only, as not every disjoint range can directly get from BITree e.g. range[2-2] is
# obtained from node2 - node1, cannot solve min/max/gcd/lcm.
#                           0(0000)
#  1(0001)  2(0010[1-2])      4(0100[1-4])                    8(1000[1-8])
#           3(0011)       5(0101) 6(0110[5-6])     9(1001) 10(1010[9-10])  12(1100[9-12])
#                                 7(0111)                  11(1011)    13(1101) 14(1110[13-14])
class NumArray(object): # USE THIS for sum
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            return
        self.__nums = [0] * len(nums)
        self.BITree = [0] * (len(self.__nums) + 1) # logic tree, physical array
        for i in range(len(nums)):
            self.update(i, nums[i])

        ''' OR write more code by a different build
        self.__nums = nums  # used to compare if update is noop
        # first calc prefix sum, then remove value of parent node.
        for i in xrange(1, len(self.BITree)):
            self.BITree[i] = nums[i-1] + self.BITree[i-1]

        for i in reversed(xrange(1, len(self.BITree))):
            last_i = i - (i & -i) # get parent by removing last set bit
            self.BITree[i] -= self.BITree[last_i] # don't store parent's value
        '''

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        delta = val - self.__nums[i]
        if delta:
            self.__nums[i] = val
            i += 1
            while i < len(self.BITree):
                self.BITree[i] += delta
                i += (i & -i) # add Last Set Bit i.e. recursively visit all larger nodes containing the value of this node

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def sum(i): # add up nodes in THIS tree branch till root
            i += 1
            ret = 0
            while i > 0:
                ret += self.BITree[i]
                i -= (i & -i) # deduct Last Set Bit = get parent, or i = i & (i-1)
            return ret
        return sum(j) - sum(i-1)


# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
# Segment Tree solutoin implemented *using an array*.
# Segment Tree is a BINARY TREE, each node is for a RANGE. ANY disjoint range can get from it,
# good for min/max/gcd/lcm. 1. Need more space than BITree. 2. query need to handle even/odd, while
# BITree needs to handle last set bit which is harder to remember.

# input [2,4,5,7,8,9] will be stored as [0,35,29,6,12,17,2,4,5,7,8,9]. All leaf nodes are for original input
# values, every two nodes merges to a "range" node (each range node has two subtrees),
# so we actually only need n-1 extra node, but we add a dummy node at begining which is convenient
# for parent-children relationship i - [2*i, 2*i+1]. The actual tree is:
#             1[6-11]
#      2[8-11]       3[6-7]
#   4[8-9] 5[10-11]  6   7
#   8   9  10   11

# 存储加倍，前半累加，每点存一disjoint区间 （build）
# 延展下标，找到兄弟sibling alway even-odd order，更新父节点 （update）
# 延展下标，分拆区间，前偶后奇向上走 （query)
class NumArray2(object): # USE THIS for min/max/gcd/lcm
    def __init__(self, nums):
        self.n = len(nums)
        self.trees = [0] * self.n + nums
        for i in reversed(range(1, self.n)):
            self.trees[i] = self.trees[2*i] + self.trees[2*i+1]

    def update(self, i, val):
        i += self.n
        delta = val - self.trees[i]
        if delta:
            while i:
                self.trees[i] += delta  # only work for sum
                i //= 2

            ''' OR
            self.trees[i] = val
            while i > 1:
                sibling = i-1 if i % 2 else i+1  # this is general for min/max/sum/gcd/lcm
                self.trees[i//2] = self.trees[i] + self.trees[sibling]
                i //= 2
            '''

    def sumRange(self, i, j):
        i += self.n
        j += self.n
        sum = 0
        while i <= j:
            if i % 2 == 1:
                sum += self.trees[i]
                i += 1
            if j % 2 == 0:
                sum += self.trees[j]
                j -= 1
            i //= 2
            j //= 2
        return sum


# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
# Segment Tree solution implemented using a tree.

class NumArray3(object):
    def __init__(self, nums,
                 query_fn=lambda x, y: x+y,
                 update_fn=lambda x, y: y,
                 default_val=0):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        N = len(nums)
        self.__original_length = N
        self.__tree_length = 2**(N.bit_length() + (N&(N-1) != 0))-1
        self.__query_fn = query_fn
        self.__update_fn = update_fn
        self.__default_val = default_val
        self.__tree = [default_val for _ in range(self.__tree_length)]
        self.__lazy = [None for _ in range(self.__tree_length)]
        self.__constructTree(nums, 0, self.__original_length-1, 0)

    def update(self, i, val):
        self.__updateTree(val, i, i, 0, self.__original_length-1, 0)

    def sumRange(self, i, j):
        return self.__queryRange(i, j, 0, self.__original_length-1, 0)

    def __constructTree(self, nums, left, right, idx):
        if left > right:
             return
        if left == right:
            self.__tree[idx] = self.__update_fn(self.__tree[idx], nums[left])
            return
        mid = left + (right-left)//2
        self.__constructTree(nums, left, mid, idx*2 + 1)
        self.__constructTree(nums, mid+1, right, idx*2 + 2)
        self.__tree[idx] = self.__query_fn(self.__tree[idx*2 + 1], self.__tree[idx*2 + 2])

    def __apply(self, left, right, idx, val):
        self.__tree[idx] = self.__update_fn(self.__tree[idx], val)
        if left != right:
            self.__lazy[idx*2 + 1] = self.__update_fn(self.__lazy[idx*2 + 1], val)
            self.__lazy[idx*2 + 2] = self.__update_fn(self.__lazy[idx*2 + 2], val)

    def __updateTree(self, val, range_left, range_right, left, right, idx):
        if left > right:
            return
        if self.__lazy[idx] is not None:
            self.__apply(left, right, idx, self.__lazy[idx])
            self.__lazy[idx] = None
        if range_left > right or range_right < left:
            return
        if range_left <= left and right <= range_right:
            self.__apply(left, right, idx, val)
            return
        mid = left + (right-left)//2
        self.__updateTree(val, range_left, range_right, left, mid, idx*2 + 1)
        self.__updateTree(val, range_left, range_right, mid+1, right, idx*2 + 2)
        self.__tree[idx] = self.__query_fn(self.__tree[idx*2 + 1],
                                           self.__tree[idx*2 + 2])

    def __queryRange(self, range_left, range_right, left, right, idx):
        if left > right:
            return self.__default_val
        if self.__lazy[idx] is not None:
            self.__apply(left, right, idx, self.__lazy[idx])
            self.__lazy[idx] = None
        if right < range_left or left > range_right:
            return self.__default_val
        if range_left <= left and right <= range_right:
            return self.__tree[idx]
        mid = left + (right-left)//2
        return self.__query_fn(self.__queryRange(range_left, range_right, left, mid, idx*2 + 1),
                               self.__queryRange(range_left, range_right, mid + 1, right, idx*2 + 2))

# Your NumArray object will be instantiated and called as such:
numArray = NumArray([2,4,5,7,8,9])
print(numArray.sumRange(0, 4)) # 26
print(numArray.sumRange(0, 1)) # 6
numArray.update(1, 10)
print(numArray.sumRange(1, 2)) # 15
