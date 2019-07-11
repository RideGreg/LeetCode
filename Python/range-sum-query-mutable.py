# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)

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

# Binary Indexed Tree (BIT) solution.
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            return
        self.__nums = nums
        self.__bit = [0] * (len(self.__nums) + 1)
        for i in xrange(1, len(self.__bit)):
            self.__bit[i] = nums[i-1] + self.__bit[i-1]

        for i in reversed(xrange(1, len(self.__bit))):
            last_i = i - (i & -i)
            self.__bit[i] -= self.__bit[last_i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if val - self.__nums[i]:
            self.__add(i, val - self.__nums[i])
            self.__nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__sum(j) - self.__sum(i-1)

    def __sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

    def __add(self, i, val):
        i += 1
        while i <= len(self.__nums):
            self.__bit[i] += val
            i += (i & -i)


# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
# Segment Tree solution implemented using a tree.

class NumArray2(object):
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


# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
# Segment Tree solutoin implemented using an array.
# input [2,4,5,7,8,9] will be stored as [0,35,29,6,12,17,2,4,5,7,8,9]. Left-right children are always even-odd indices of the underlying array.

class NumArray3(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.trees = [0] * self.n + nums
        for i in reversed(range(1, self.n)):
            self.trees[i] = self.trees[2*i] + self.trees[2*i+1]

    def update(self, i, val):
        i += self.n
        if self.trees[i] == val: return

        self.trees[i] = val
        while i > 1:
            sibling = i-1 if i % 2 else i+1  # this is general for min/max/sum/gcd/lcm
            self.trees[i/2] = self.trees[i] + self.trees[sibling]
            i /= 2

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
            i /= 2
            j /= 2
        return sum

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
