# Time:  O(nlogn)
# Space: O(n)

# 315
# You are given an integer array nums and you have to
# return a new counts array. The counts array has the
# property where counts[i] is the number of smaller
# elements to the right of nums[i].
#
# Example:
#
# Given nums = [5, 2, 6, 1]
#
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].


# Time:  O(nlogn)
# Space: O(n)
# BIT solution. OK for smaller/larger/smaller+eq/larger+eq numbers before/after self.
# Don't do linear scan to see how many valid numbers already seen, which results in O(n^2).
#
# Use a helper data structure BITree to store how many numbers before THIS place were seen. Two key things:
# 1. Pre-process to find the position of each number in sorted array. 2. each number -> its place -> a node in BITree;
# after seeing a number at place[i], increment all BITree nodes corresponding PLACES AFTER i by 1.
# underlying list of BITree [dummy, 0, 0, 0, 0, 0]
# seeing 4th number -> [dummy, 0, 0, 0, 1, 0]
# seeing 2nd number -> [dummy, 0, 1, 0, 2, 0]
# seeing 1st number -> [dummy, 1, 2, 0, 3, 0]

# 树状数组 + 离散化
# 树状数组可以动态维护序列前缀和。记题目给定的序列为a，我们用桶来表示值域中的每一个数，桶中记录这些数字出现的次数。
# 假设a={5,5,2,3,6}，那么遍历这个序列得到的桶是这样的：
# index  ->  1 2 3 4 5 6 7 8 9
# value  ->  0 1 1 0 2 1 0 0 0
# value序列第i-1位的前缀和表示「有多少个数比 i小」。动态维护前缀和的问题我们可以用「树状数组」来解决。

# 用离散化优化空间
# 如果a值域很大，value序列很多位置是0。用离散化的方法减少无效位置出现。将原数组去重后排序，
# 原数组每个数映射到去重排序后这个数对应位置的下标
class Solution(object): # USE THIS,
    def countSmaller(self, nums, compare="smaller", dir="right"):
        """
        :type nums: List[int]
        :type compare: str - this is a param I add to test "smaller" vs "smaller and equal to"
        :rtype: List[int]
        """
        class BIT(object):
            def __init__(self, n):
                self.__bit = [0] * (n + 1)

            def add(self, i, val): # always increment 1, so no need to write update()
                i += 1
                while i < len(self.__bit):
                    self.__bit[i] += val
                    i += (i & -i)

            def query(self, i): # query前缀和，相当于range_sum[0..i]
                i += 1
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    i -= (i & -i)
                return ret

        # Get the place (position in the ascending order) of each unique number.
        # If asking larger numbers, sort in descending order.
        sorted_nums = sorted(set(nums))
        places = {x: i for i, x in enumerate(sorted_nums)}
        bit = BIT(len(places))
        ans = [0] * len(nums)

        # Asks "after self", scan from right to left. For "before self", scan from left.
        iterable = range(len(nums)) if dir == 'left' else reversed(range(len(nums)))
        for i in iterable:
            x = nums[i]
            if compare == "smaller":
                ans[i] = bit.query(places[x] - 1) # places[x] is self, for all smaller num, query places[x]-1
            elif compare == "smaller_eq":
                ans[i] = bit.query(places[x])

            bit.add(places[x], 1) # after visit a num, increment self node and all nodes including it
        return ans

# Divide and Conquer solution.
class Solution2(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def countAndMergeSort(start, end):
            if start >= end:  # The size of range [start, end] less than 2 is always with count 0.
                return 0

            mid = start + (end - start) // 2
            countAndMergeSort(start, mid)
            countAndMergeSort(mid + 1, end)
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                # Merge the two sorted arrays into tmp.
                while r <= end and num_idxs[r][0] < num_idxs[i][0]:
                    tmp.append(num_idxs[r])
                    r += 1
                tmp.append(num_idxs[i])
                counts[num_idxs[i][1]] += r - (mid + 1)

            # Copy tmp back to num_idxs
            num_idxs[start:start+len(tmp)] = tmp

        num_idxs = []
        counts = [0] * len(nums)
        for i, num in enumerate(nums):
            num_idxs.append((num, i))
        countAndMergeSort(0, len(num_idxs) - 1)
        return counts

    def countSmaller_wrong_merge(self, nums): # this implementation has bug, need to find out!!
        def countAndMergeSort(start, end):
            if start >= end:  return 0

            mid = start + (end - start) // 2
            countAndMergeSort(start, mid)
            countAndMergeSort(mid + 1, end)
            # first pass count reverse paris
            r = mid + 1
            for i in range(start, mid + 1):
                while r <= end and nums[r] < nums[i]:
                    r += 1
                counts[i] += r - (mid + 1)
            # second pass do merge
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                # Merge the two sorted arrays into tmp.
                while r <= end and nums[r] < nums[i]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[i])
            # Copy tmp back to num_idxs
            nums[start:start+len(tmp)] = tmp

        counts = [0] * len(nums)
        countAndMergeSort(0, len(nums) - 1)
        return counts


# Time:  O(nlogn) ~ O(n^2)
# Space: O(n)
# BST solution.
class Solution3(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        bst = self.BST()
        # Insert into BST and get left count.
        for i in reversed(range(len(nums))):
            bst.insertNode(nums[i])
            res[i] = bst.query(nums[i])

        return res

    class BST(object):
        class BSTreeNode(object):
            def __init__(self, val):
                self.val = val
                self.count = 0
                self.left = self.right = None

        def __init__(self):
            self.root = None

        # Insert node into BST.
        def insertNode(self, val):
            node = self.BSTreeNode(val)
            if not self.root:
                self.root = node
                return
            curr = self.root
            while curr:
                # Insert left if smaller.
                if node.val < curr.val:
                    curr.count += 1  # Increase the number of left children.
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        break
                else:  # Insert right if larger or equal.
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        break

        # Query the smaller count of the value.
        def query(self, val):
            count = 0
            curr = self.root
            while curr:
                # Insert left.
                if val < curr.val:
                    curr = curr.left
                elif val > curr.val:
                    count += 1 + curr.count  # Count the number of the smaller nodes.
                    curr = curr.right
                else:  # Equal.
                    return count + curr.count
            return 0

print(Solution().countSmaller([5,2,6,1])) # [2,1,1,0]
print(Solution().countSmaller([1,1,6,2,5,2,0,2])) # [1,1,5,1,3,1,0,0]
print(Solution().countSmaller([1,1,6,2,5,2,0,2], "smaller")) # [1,1,5,1,3,1,0,0]
print(Solution().countSmaller([1,1,6,2,5,2,0,2], "smaller_eq")) # [2,1,5,3,3,2,0,0]
print(Solution().countSmaller([1,1,6,2,5,2,0,2], "smaller", "left")) # [0,0,2,2,3,2,0,3]
