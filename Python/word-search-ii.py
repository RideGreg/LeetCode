# Time:  O(m * n * (3^l))), l is max length of any word. For each starting cell, worst case
#     travel l steps, each step has 3 neighbors except the first step which has 4 directions.
# Space: O(N), 字典中的字母总数。In worst case if there is no prefix overlap, trie has same # of nodes
#              as all characters from all words.

# 212
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#


# Soluton: Trie + backtracking 使用前缀树的回溯
# - Q: Why store words in Trie, not just iterate words?
# - A: Since we may have a lot of words that can be highly similar ['abcdefx', 'abcdefy'], don't repeat computation.
# Consider the case where board = ['a', 'b', 'c', 'd'], words = ['abca', 'abcb', ... 'abcz...]
# Traverse board and compare to Trie: traverse only once, which is much much less work
# than traverse N words which traverses board N times.

# 问题实际上是一个简化的纵横填字游戏，解决问题的关键在于如何从字典中找到单词的匹配项，一般使用Python set。
# 优化：格子上每条路径是否需要走到头，就是说检查包含特定前缀的单词，而不是是否有整个字符串作为单词存在于字典中。因为如果知道
# 给定前缀的字典中不存在任何单词匹配，我们就不需要进一步探索某个方向，这将大大减少探测空间，提高回溯算法的性能。
# 能够查找前缀的数据结构叫 Trie。

# 进一步优化：1. 在回溯过程中逐渐剪除 Trie 中的节点（剪枝）。
# 这个想法的动机是算法的时间复杂度取决于 Trie 的大小。对于 Trie 中的叶节点，一旦遍历它（即找到匹配的单词），就不需要再遍历它了，
# 我们可以把它从树上剪下来。逐渐地，这些非叶节点可以成为叶节点，因为我们剪掉了他们的孩子叶节点。在极端情况下，一旦我们找到字典
# 中所有单词的匹配项，Trie 就会变成空的。
#
# 2. 从 Trie 中删除匹配的单词。
# 此问题我们被要求返回所有匹配的单词，而不是潜在匹配的数量。因此，一旦到达包含单词匹配的特定 Trie 节点，我们就可以从 Trie
# 中删除匹配单词。好处在于我们不需要检查结果集中是否有任何重复项。因此，可以使用一个列表而不是集合来保存结果，加快解决方案的速度。

class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}   # better to use collections.defaultdict

    # Inserts a word into the trie.
    def insert(self, word): # call this method on a root node object, or define the method in a Trie class with a root node member.
        cur = self
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(node, i, j, cur_word):
            # 如果只有判断(i,j)是否valid，可以放在recursive call dfs之前。
            # 如果有更多check，还是全部放此处最好。
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] not in node.leaves:
                return

            cur_word.append(board[i][j])
            next_node = node.leaves[board[i][j]]
            if next_node.is_string:
                ans.add("".join(cur_word))

            letter = board[i][j]
            board[i][j] = '#' # mark as visited
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(next_node, i + di, j + dj, cur_word)
            board[i][j] = letter
            cur_word.pop()

        # build trie
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        # start with each cell
        m, n, ans = len(board), len(board[0]), set()
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j, [])
        return list(ans)


board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
print(Solution().findWords(board, ["oath","pea","eat","rain"])) # ["eat","oath"]
print(Solution().findWords([['a', 'a']], ['a'])) # ['a']