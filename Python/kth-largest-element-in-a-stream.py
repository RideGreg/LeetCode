'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element
in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream. For each call to the method KthLargest.add,
return the element representing the kth largest element in the stream.

Example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length >= k-1 and k >= 1.
'''

# not run in Leetcode. Maintain counter on BST node.
class MyTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.rightCnt = 0


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.root = None
        for n in nums:
            self.root = self.insert(self.root, n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.root = self.insert(self.root, val)
        return self.kthLargest()

    def insert(self, root, v):
        if not root:
            root = MyTreeNode(v)
            return root

        p = root
        while p:
            if v <= p.val:
                if p.left:
                    p = p.left
                else:
                    p.left = MyTreeNode(v)
                    return root
            else:
                p.rightCnt += 1
                if p.right:
                    p = p.right
                else:
                    p.right = MyTreeNode(v)
                    return root

    def kthLargest(self):
        p, kk = self.root, self.k
        while p:
            if kk < p.rightCnt + 1:
                p = p.right
            elif kk > p.rightCnt + 1:
                kk -= (p.rightCnt + 1)
                p = p.left
            else:
                return p.val

# TLE.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class KthLargest_bst(object): # good for balanced tree
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.root = None
        for n in nums:
            self.root = self.insert(self.root, n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.root = self.insert(self.root, val)
        return self.kthLargest()

    def insert(self, root, v):
        if not root:
            root = TreeNode(v)
            return root

        p = root
        while p:
            if v < p.val:
                if p.left: p = p.left
                else:
                    p.left = TreeNode(v)
                    return root
            else:
                if p.right: p = p.right
                else:
                    p.right = TreeNode(v)
                    return root
        ''' maximum recursion depth exceeded for more than 1000 levels
        if not node:
            return TreeNode(v)
        if v <= node.val:
            node.left = self.insert(node.left, v)
        else:
            node.right = self.insert(node.right, v)
        return node
        '''

    def kthLargest(self):
        def pushRight(node):
            while node:
                stack.append(node)
                node = node.right

        stack = []
        pushRight(self.root)
        m = 0
        while stack and m < self.k:
            cur = stack.pop()
            m += 1
            pushRight(cur.left)
        return cur.val


# USE THIS
# TLE. Heap is size n, so when having more numbers, slower and slower, each add O(logn + nlogk).
# Unfortunately cannot use a size-k Heap, because all numbers stream in need to be kept to get kth largest correctly.
# https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library
# https://stackoverflow.com/questions/29109741/what-is-the-time-complexity-of-getting-first-n-largest-elements-in-min-heap?lq=1
import heapq
class KthLargest_heapSizeN(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.h = nums
        heapq.heapify(self.h)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.h, val)
        return heapq.nlargest(self.k, self.h)[-1] 
        


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4,5,8,2])
print obj.add(3) #4
print obj.add(5) #5
print obj.add(10) #5
print obj.add(9) #8
print obj.add(4) #8

import timeit
# 1.76037311554 vs 1.70498609543 vs 0.570573806763
obj = KthLargest(20, range(500,510)+range(50,60))
obj2 = KthLargest_bst(20, range(500,510)+range(50,60))
obj3 = KthLargest_heapSizeN(20, range(500,510)+range(50,60))
print timeit.timeit("for x in range(1500): obj.add(x)", "from __main__ import obj", number=1)
print timeit.timeit("for x in range(1500): obj2.add(x)", "from __main__ import obj2", number=1)
print timeit.timeit("for x in range(1500): obj3.add(x)", "from __main__ import obj3", number=1)

# skewed tree, k = 1: 3.57821202278 vs. 3.08418989182 vs. 0.032653093338
obj = KthLargest(1, [])
obj2 = KthLargest_bst(1, [])
obj3 = KthLargest_heapSizeN(1, [])
print timeit.timeit("for x in range(1500): obj.add(x)", "from __main__ import obj", number=1)
print timeit.timeit("for x in range(1500): obj2.add(x)", "from __main__ import obj2", number=1)
print timeit.timeit("for x in range(1500): obj3.add(x)", "from __main__ import obj3", number=1)

# skewed tree, k = 2: 3.24866390228 vs. 3.1738409996 vs. 0.22509598732
obj = KthLargest(2, [1])
obj2 = KthLargest_bst(2, [1])
obj3 = KthLargest_heapSizeN(2, [1])
print timeit.timeit("for x in range(1500): obj.add(x)", "from __main__ import obj", number=1)
print timeit.timeit("for x in range(1500): obj2.add(x)", "from __main__ import obj2", number=1)
print timeit.timeit("for x in range(1500): obj3.add(x)", "from __main__ import obj3", number=1)
