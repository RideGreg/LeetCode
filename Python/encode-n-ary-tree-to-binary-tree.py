'''
N-ary tree => binary tree: for each node, first sibling becomes left child, first child becomes right child.
For example, you may encode the following N-ary tree
      1
    / | \
   2  3  4
     / \  \
    5  6  7

into a binary tree (or its mirror)
     1
      \
      2
     /
    3
   / \
  4   5
   \  /
   7  6

https://leetcode.com/articles/introduction-to-n-ary-trees/
https://groups.google.com/forum/#!topic/wncc_iitb/RrgohUZ-uhw
1. Create L to R sibling pointers at each level
2. Remove all but the leftmost child pointer of each node
3. Make the sibling pointer the right pointer.

https://www.careercup.com/question?id=6486564775395328
any N-ary tree can convert to a 1-D array

https://stackoverflow.com/questions/16911521/convert-an-n-ary-expression-tree-to-a-binary-tree
no contents
https://www.educative.io/collection/page/5642554087309312/5679846214598656/820001/preview
need to pay
https://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/

'''