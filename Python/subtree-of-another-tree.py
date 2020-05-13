# Time:  O(m * n), m is the number of nodes of s, n is the number of nodes of t
# Space: O(h), h is the height of s

# Given two non-empty binary trees s and t,
# check whether tree t has exactly the same structure and
# node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#      3
#     / \
#   4   5
#   / \
#  1   2
# Given tree t:
#   4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#   4   5
#   / \
#  1   2
#     /
#   0
# Given tree t:
#   4
#   / \
#  1   2
# Return false.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # DFS 暴力匹配
    # 最朴素的方法 —— DFS 枚举 s 中的每一个节点，判断这个点的子树是否和t相等。为了判断一个节点的子树是否和 t相等，
    # 又需要做一次DFS，即让两个指针一开始先指向该节点和t的根，然后同步移动两根指针来「同步遍历」这两棵树，判断对应位置是否相等。

    # Time：对于每一个s上的点，都需要做一次 DFS来和t匹配，匹配一次的时间代价是 O(|t|)，那么总的时间代价就是 O(∣s∣×∣t∣)。
    # Space：假设s 深度为 d_s，t的深度为 d_t，任意时刻栈空间的最大使用代价是O(max{d_s, d_t})。
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)

        # dfs
        stk = [s]
        while stk:
            node = stk.pop()
            if node:
                if isSame(node, t): return True
                stk.append(node.left)
                stk.append(node.right)
        return False

    # DFS序列上做串匹配
    # 一棵子树上的点在 DFS 序列（即先序遍历）中是连续的。所以可以把s和t先转换成 DFS 序，然后看 t的 DFS 序是否是 s的
    # DFS 序的「子串」。
    # 这样做正确吗？ 假设 s由两个点组成1是根，2是 1的左孩子；t也由两个点组成，1是根，2是 1的右孩子。
    # 这样一来s和t的DFS序相同，可是t并不是s的某一棵子树。由此可见「s的 DFS序包含 t的 DFS序」是「t是 s子树」的必要不充分条件，
    # 所以需要引入两个空值 lNull和 rNull，当一个节点的左孩子或右孩子为空的时候，就插入这两个空值，这样 DFS序列就唯一对应一棵树。
    # 处理完之后，就可以通过判断 「s的 DFS 序包含 t的 DFS 序」来判断答案。
    #
    # Time: 遍历两棵树得到 DFS 序列的时间代价是 O(|s| + |t|)，在匹配的时候，如果使用暴力匹配，时间代价为 O(∣s∣×∣t∣)，
    # 使用 KMP 或 Rabin-Karp 进行串匹配的时间代价都是 O(|s| + |t|)。由于这里使用 KMP 实现，所以渐进时间复杂度为 O(|s| + |t|)。
    # Space: 保存了两个 DFS 序列，还计算了 |t|长度的 fail 数组，辅助空间的总代价为 O(|s| + |t|)，任意时刻栈空间的最大使用
    # 代价是 O(max{ d_s, d_t})，由于 $ max{d_s, d_t} = O(|s| + |t|)，故渐进空间复杂度为 O(|s| + |t|)。
    ''' C++
class Solution {
public:
    vector <int> sOrder, tOrder;
    int maxElement, lNull, rNull;

    void getMaxElement(TreeNode *o) {
        if (!o) return;
        maxElement = max(maxElement, o->val);
        getMaxElement(o->left);
        getMaxElement(o->right);
    }

    void getDfsOrder(TreeNode *o, vector <int> &tar) {
        if (!o) return;
        tar.push_back(o->val);
        if (o->left) getDfsOrder(o->left, tar);
        else tar.push_back(lNull);
        if (o->right) getDfsOrder(o->right, tar);
        else tar.push_back(rNull);
    }

    bool kmp() {
        int sLen = sOrder.size(), tLen = tOrder.size();
        vector <int> fail(tOrder.size(), -1);
        for (int i = 1, j = -1; i < tLen; ++i) {
            while (j != -1 && tOrder[i] != tOrder[j + 1]) j = fail[j];
            if (tOrder[i] == tOrder[j + 1]) ++j;
            fail[i] = j;
        }
        for (int i = 0, j = -1; i < sLen; ++i) {
            while (j != -1 && sOrder[i] != tOrder[j + 1]) j = fail[j];
            if (sOrder[i] == tOrder[j + 1]) ++j;
            if (j == tLen - 1) return true;
        }
        return false;
    }

    bool isSubtree(TreeNode* s, TreeNode* t) {
        maxElement = INT_MIN;
        getMaxElement(s);
        getMaxElement(t);
        lNull = maxElement + 1;
        rNull = maxElement + 2;

        getDfsOrder(s, sOrder);
        getDfsOrder(t, tOrder);

        return kmp();
    }
};
    '''