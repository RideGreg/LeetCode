# Time:  O(logn)
# Space: O(logn)

# 1104
# In an infinite binary tree where every node has two children, nodes are labelled in row order.
#
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right,
# while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
#                 1
#         3               2
#     4       5       6      7
#  15  14  13  12  11  10  9  8
#
# Given the label of a node in this tree, return the labels in the path from the root of
# the tree to the node with that label.

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        count = 2**label.bit_length()
        ans = []
        while label >= 1:
            ans.append(label)
            begin, end = count // 2, count - 1
            label = (begin + (end-label)) // 2
            count //= 2
        return ans[::-1]

    def pathInZigZagTree_ming(self, label): # similar but can improve over the above,
                                         # bit_length on each row doesn't need to campute each time
        ans = [label]
        while label > 1:
            k = label // 2
            b = k.bit_length()
            s, e = 2**(b-1), 2**b - 1
            label = s + (e - k)
            ans.append(label)
        ans.append(label)
        return ans[::-1]

print(Solution().pathInZigZagTree(14)) # [1,3,4,14]
print(Solution().pathInZigZagTree(26)) # [1,2,6,10,26]