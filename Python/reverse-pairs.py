# Time:  O(nlogn)
# Space: O(n)

# 493
# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.


class Solution(object):
    def reversePairs(self, nums): # USE THIS: BIT
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        class BIT(object):
            def __init__(self, n):
                self.bit = [0]*(n+1)
            def add(self, i):
                i += 1
                while i < len(self.bit):
                    self.bit[i] += 1
                    i += i & (-i)
            def query(self, i):
                i += 1
                ans = 0
                while i > 0:
                    ans += self.bit[i]
                    i -= i & (-i)
                return ans

        st = sorted(set(nums))
        lookup = {x: i for i, x in enumerate(st)}
        ans, bit = 0, BIT(len(st))
        for i in reversed(range(len(nums))):
            x = nums[i]
            pos = bisect.bisect_left(st, x/2) # nums[i] > 2*nums[j], pos for query cannot directly use lookup[x]
            ans += bit.query(pos-1)
            bit.add(lookup[x])
        return ans

    def reversePairs_mergesort(self, nums):  # this seems working
        def merge(start, mid, end):
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[i])
            nums[start:start+len(tmp)] = tmp

        def countAndMergeSort(start, end):
            if end - start <= 0:
                return 0

            mid = start + (end - start) / 2
            count = countAndMergeSort(start, mid) + countAndMergeSort(mid + 1, end)
            # first pass to count reverse pairs
            r = mid + 1
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r] * 2:
                    r += 1
                count += r - (mid + 1)
            # second pass do merge
            merge(start, mid, end)
            return count

        return countAndMergeSort(nums, 0, len(nums) - 1)

    def reversePairs_my_mergesort(self, nums): # use this for merge sort
        def merge(left, right):
            ans = []
            # need to count reverse first, otherwise the reverse pair gets lost e.g. [2,4], [1,3] where 4>2*1
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2*right[j]:
                    j += 1
                self.count += j

            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    ans.append(right[j])
                    j += 1
                else:
                    ans.append(left[i])
                    i += 1
            ret= ans + left[i:len(left)] + right[j:len(right)]
            return ret

        def merge_sort(arr):
            if len(arr) <= 1: return arr
            mid = len(arr) // 2
            l, r = merge_sort(arr[:mid]), merge_sort(arr[mid:])
            return merge(l, r)

        self.count = 0
        merge_sort(nums)
        return self.count


class Node:
    def __init__(self, x):
        self.val = x
        self.greater_eq = 1
        self.left = None
        self.right = None

class Solution_BST: #TLE: BST tree can be skewed hence, making it O(n^2) in complexity
    def reversePairs(self, nums):
        def search(head, value):
            if not head: return 0
            elif value == head.val: return head.greater_eq
            elif value < head.val:
                return head.greater_eq + search(head.left, value)
            else:
                return search(head.right, value)

        def insert(head, value):
            if not head:
                return Node(value)
            elif value == head.val:
                head.greater_eq += 1
            elif value < head.val:
                head.left = insert(head.left, value)
            else:
                head.greater_eq += 1
                head.right = insert(head.right, value)
            return head

        ans, head = 0, None
        for n in nums:
            ans += search(head, 2 * n + 1)
            head = insert(head, n)

        return ans


print(Solution().reversePairs([1,3,2,3,1])) # 2
print(Solution().reversePairs([2,4,3,5,1])) # 3