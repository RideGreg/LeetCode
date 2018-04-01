class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.val = 0
        self.leaves = {}

class Solution:
    """
    @param nums: the array
    @return: the max xor sum of the subarray in a given array
    """
    def maxXorSubarray(self, nums):
        def insert(root, n):
            for i in reversed(xrange(32)):
                val = (n>>i) & 1
                if val not in root.leaves:
                    root.leaves[val] = TrieNode()
                root = root.leaves[val]
            root.val = n

        def query(root, n):
            for i in reversed(xrange(32)):
                val = (n>>i) & 1
                if 1-val in root.leaves:
                    root = root.leaves[1-val]
                elif val in root.leaves:
                    root = root.leaves[val]
            return n^root.val


        root = TrieNode()
        insert(root, 0)
        ans, cur = 0, 0
        for num in nums:
            cur = cur^num
            insert(root, cur)
            ans = max(ans, query(root, cur))
        return ans

#print Solution().maxXorSubarray([8,2,1,12])
print Solution().maxXorSubarray([1,2,3,4])
print Solution().maxXorSubarray([8,1,2,12,7,6])
print Solution().maxXorSubarray([4,6])

