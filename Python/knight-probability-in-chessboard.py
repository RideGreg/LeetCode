# Time:  O(k * n^2)
# Space: O(n^2)

# 688
# On an NxN chessboard, a knight starts at the r-th row and c-th column and
# attempts to make exactly K moves. The rows and columns are 0 indexed,
# so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
#
# A chess knight has 8 possible moves it can make, as illustrated below.
# Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
#
# Each time the knight is to move, it chooses one of eight possible moves uniformly
# at random (even if the piece would go off the chessboard) and moves there.
#
# The knight continues moving until it has made exactly K moves or has moved off the chessboard.
# Return the probability that the knight remains on the board after it has stopped moving.
#
# Example:
# Input: 3, 2, 0, 0
# Output: 0.0625
#
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
#
# Note:
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.

class Solution(object):
    # bookshadow: use dict to save time/space, since we only care the cells we can reach last time
    def knightProbability(self, N, K, r, c): # USE THIS
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        import collections
        dirs = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
        ans = 0
        dmap = {(r, c) : 1}
        for t in range(K):
            dmap0 = collections.defaultdict(int)
            for (x, y), pb in dmap.items():
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        ans += 0.125 * pb
                    else:
                        dmap0[(nx, ny)] += 0.125 * pb
            dmap = dmap0
        return 1 - ans


    def knightProbability_fullSpace(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1.0
        dirs = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
        not_in = 0 # complimentary probability
        for _ in range(K):
            ndp = [[0] * N for _ in range(N)]
            for x in range(N):
                for y in range(N):
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<N and 0<=ny<N:
                            ndp[nx][ny] += 0.125 * dp[x][y]
                        else:
                            not_in += 0.125 * dp[x][y]
            dp = ndp
        return 1 - not_in


print(Solution().knightProbability(3,2,0,0)) # 0.0625