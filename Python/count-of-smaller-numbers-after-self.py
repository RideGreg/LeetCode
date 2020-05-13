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

# Time:  O(nlogn)
# Space: O(n)
# BIT solution. OK for smaller/larger/smaller+eq/larger+eq numbers before/after self.
# Don't do linear scan to see how many valid numbers already seen, which results in O(n^2).
#
# Use a helper data structure BITree to store what numbers were seen. Two extra things:
# 1. Pre-process to find the position of each number in sorted array. 2. each number maps to a node in BITree;
# after seeing a number, increment all BITree nodes (before and include the mapping noce) by 1.
# underlying list of BITree [dummy, 0, 0, 0, 0, 0]
# seeing 4th number -> [dummy, 0, 0, 0, 1, 0]
# seeing 2nd number -> [dummy, 0, 1, 0, 2, 0]
# seeing 1st number -> [dummy, 1, 2, 0, 3, 0]
class Solution(object): # USE THIS,
    def countSmaller(self, nums, compare="smaller", dir="right"):
        """
        :type nums: List[int]
        :type compare: str - this is a param I add to test "smaller" vs "smaller and equal to"
        :rtype: List[int]
        """
        import bisect
        class BIT(object):
            def __init__(self, n):
                self.__bit = [0] * n

            def add(self, i, val):
                while i < len(self.__bit):
                    self.__bit[i] += val
                    i += (i & -i)

            def query(self, i):
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    i -= (i & -i)
                return ret

        # Get the place (position in the ascending order) of each number.
        # If asking larger numbers, sort in descending order.
        sorted_nums, places = sorted(nums), [0] * len(nums)
        for i, num in enumerate(nums):
            places[i] = bisect.bisect_left(sorted_nums, num)

        ans, bit= [0] * len(nums), BIT(len(nums) + 1)

        # Asks "after self", scan from right to left. For "before self", scan from left.
        iterable = range(len(nums)) if dir == 'left' else reversed(range(len(nums)))
        for i in iterable:
            if compare == "smaller":
                ans[i] = bit.query(places[i]) # places[i]+1 is self, for all smaller num, query places[i]
            elif compare == "smaller_eq":
                ans[i] = bit.query(places[i] + 1)

            bit.add(places[i] + 1, 1) # after visit a num, increment self node and all nodes including it
        return ans

# Time:  O(nlogn)
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
print(Solution().countSmaller([1,1,6,2,5,2,0,2], "smaller")) # [1,1,5,1,3,1,0,0]
print(Solution().countSmaller([1,1,6,2,5,2,0,2], "smaller_eq")) # [2,1,5,3,3,2,0,0]
print(Solution().countSmaller([1,1,6,2,5,2,0,2], "smaller", "left")) # [0,0,2,2,3,2,0,3]
