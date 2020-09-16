# Time:  O(m * n * l)
# Space: O(l)
# 79
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   "ABCE",
#   "SFCS",
#   "ADEE"
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
#

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(i, x, y):
            if i == len(word): return True

            # all "if check" merges here. Since we change to '#' for visited cell,
            # this filters both visited cell and non-match char.
            if not (0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == word[i]):
                return False

            letter = board[x][y]
            board[x][y] = '#' # mark as visited
            for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if dfs(i+1, nx, ny):
                    return True
            board[x][y] = letter
            return False

        return any(dfs(0, x, y) for x in range(len(board)) for y in range(len(board[0])))


    def exist_kamyu(self, board, word):
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.existRecu(board, word, 0, i, j, visited):
                    return True

        return False

    def existRecu(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i - 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i, j + 1, visited) or\
                 self.existRecu(board, word, cur + 1, i, j - 1, visited)
        visited[i][j] = False

        return result

if __name__ == "__main__":
    board = [
              ["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]
            ]
    print(Solution().exist(board, "ABCCED")) # True
    print(Solution().exist(board, "SFCS")) # True
    print(Solution().exist(board, "ABCB")) # False
