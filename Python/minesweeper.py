# Time:  O(m * n)
# Space: O(m + n) ? or O(m*n) put (up to) all elements in the queue

# 529
# Let's play the minesweeper game (Wikipedia, online game)!
#
# You are given a 2D char matrix representing the game board. 'M' represents an UNREVEALED mine,
# 'E' represents an UNREVEALED empty square, 'B' represents a REVEALED blank square that has no adjacent
# (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents
# how many mines are adjacent to this REVEALED square, and finally 'X' represents a REVEALED mine.
#
# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
# return the board after revealing this position according to the following rules:
#
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B')
# and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
# representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
#
# 对于当前需要点击的点，我们先判断是不是雷，是的话直接标记X返回即可。如果不是的话，我们就数该点周围的雷个数，如果周围有雷，
# 则当前点变为雷的个数并返回。如果没有的话，我们再对周围所有的点调用递归函数再点击即可
#
# Example 1:
# Input:
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
# Click : [3,0]
# Output:
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Example 2:
# Input:
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Click : [1,2]
# Output:
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Note:
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'),
# which also means the input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been revealed).
# For simplicity, not mentioned rules should be ignored in this problem.
# For example, you don't need to reveal all the unrevealed mines when the game is over,
# consider any cases that you will win the game or flag any squares.

import collections

# BFS
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        q = collections.deque([click])
        while q:
            row, col = q.popleft()
            if board[row][col] == 'M':
                board[row][col] = 'X'
                break
            else:
                count, nei = 0, []      # remember empty neighbors to avoid the second iteration
                for i in range(-1, 2):  # much conciser than listing 8 new points
                    for j in range(-1, 2):
                        r, c = row + i, col + j
                        if (i != 0 or j != 0) and 0 <= r < len(board) and 0 <= c < len(board[r]):
                            if board[r][c] in 'MX':
                                count += 1
                            elif board[r][c] == 'E' and count == 0:
                                nei.append((r, c))

                if count:
                    board[row][col] = str(count)
                else:
                    board[row][col] = 'B'
                    for r, c in nei:
                        q.append((r, c))
                        board[r][c] = ' ' # avoid duplicate adding cell to the queue

        return board


print(Solution().updateBoard([
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']
], [3, 0]))
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

print(Solution().updateBoard([
    ['B', '1', 'E', '1', 'B'],
    ['B', '1', 'M', '1', 'B'],
    ['B', '1', '1', '1', 'B'],
    ['B', 'B', 'B', 'B', 'B']
], [1, 2]))
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]