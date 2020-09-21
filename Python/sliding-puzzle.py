# Time:  O((m * n) * (m * n)!)
# Space: O((m * n) * (m * n)!)

# 773
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
#
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
#
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
#
# Given a puzzle board, return the least number of moves required
# so that the state of the board is solved. If it is impossible
# for the state of the board to be solved, return -1.
#
# Examples:
#
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
#
# Note:
# - board will be a 2 x 3 array as described above.
# - board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

import collections, heapq, itertools
from typing import List

class Solution(object):
    # BFS. Optimization can save position of 0 in queue (together with state and step)
    # so don't need to search position of 0 in each iteration.
    def slidingPuzzle(self, board: List[List[int]]) -> int:          # USE THIS: simpler
        cur = [str(x) for x in board[0] + board[1]]
        src = ''.join(cur)
        dst = '123450'

        q = collections.deque([(src, 0)]) # state, step
        seen = {src}
        while q:
            state, step = q.popleft()
            if state == dst:
                return step

            pos = state.index('0')  # this info can save to queue for optimization
            x, y = divmod(pos, 3)
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0<=nx<2 and 0<=ny<3:
                    new_pos = nx*3 + ny
                    arr = list(state)
                    arr[pos], arr[new_pos] = arr[new_pos], arr[pos]
                    new_state = ''.join(arr)
                    if new_state not in seen:
                        seen.add(new_state)
                        q.append((new_state, step+1))
        return -1


# Time:  O((m * n) * (m * n)! * log((m * n)!))
# Space: O((m * n) * (m * n)!)
# A* Search Algorithm
# 对于每个节点，定义一个预估代价 node.priority = node.depth + node.heuristic，其中 node.depth 为已经走过的距离，
# node.heuristic 为预估的剩余距离。
#
# 对于熟悉 Dijkstra 算法 的读者来说，可以把 Dijkstra 算法 当成一种在 node.heuristic = 0 情况下 A* 搜索算法 的特例。
# 在一些特定的图中，A* 搜索算法 是要比深度优先搜索更快的。
#
# 每个节点代表一种棋盘的状态。保持一个优先队列，根据 node.depth + node.heuristic 排序。预估的剩余距离为每个节点到终点
# 的曼哈顿距离。对于初始状态的棋盘，有可能解开谜题，也有可能解不开谜题。为了加快算法，定义 targetWrong，
# 如果进入这种状态是一定不能到达终点的，也就不用继续搜便下去了。这里其实是可以证明，除了最后两块其他块是一定能
# 放到正确的位置上的。具体证明可以看这个链接 http://kevingong.com/Math/SixteenPuzzle.html.

class Solution2(object):
    def slidingPuzzle(self, board):
        def dot(p1, p2):
            return p1[0]*p2[0]+p1[1]*p2[1]

        def heuristic_estimate(board, R, C, expected):
            result = 0
            for i in xrange(R):
                for j in xrange(C):
                    val = board[C*i + j]
                    if val == 0: continue
                    r, c = expected[val]
                    result += abs(r-i) + abs(c-j)
            return result

        R, C = len(board), len(board[0])
        begin = tuple(itertools.chain(*board))
        end = tuple(range(1, R*C) + [0])
        expected = {(C*i+j+1) % (R*C) : (i, j)
                    for i in xrange(R) for j in xrange(C)}

        min_steps = heuristic_estimate(begin, R, C, expected)
        closer, detour = [(begin.index(0), begin)], []
        lookup = set()
        while True:
            if not closer:
                if not detour:
                    return -1
                min_steps += 2
                closer, detour = detour, closer
            zero, board = closer.pop()
            if board == end:
                return min_steps
            if board not in lookup:
                lookup.add(board)
                r, c = divmod(zero, C)
                for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    i, j = r+direction[0], c+direction[1]
                    if 0 <= i < R and 0 <= j < C:
                        new_zero = i*C+j
                        tmp = list(board)
                        tmp[zero], tmp[new_zero] = tmp[new_zero], tmp[zero]
                        new_board = tuple(tmp)
                        r2, c2 = expected[board[new_zero]]
                        r1, c1 = divmod(zero, C)
                        r0, c0 = divmod(new_zero, C)
                        is_closer = dot((r1-r0, c1-c0), (r2-r0, c2-c0)) > 0
                        (closer if is_closer else detour).append((new_zero, new_board))
        return min_steps


    def slidingPuzzle2(self, board):
        def heuristic_estimate(board, R, C, expected):
            result = 0
            for i in xrange(R):
                for j in xrange(C):
                    val = board[C*i + j]
                    if val == 0: continue
                    r, c = expected[val]
                    result += abs(r-i) + abs(c-j)
            return result

        R, C = len(board), len(board[0])
        begin = tuple(itertools.chain(*board))
        end = tuple(range(1, R*C) + [0])
        end_wrong = tuple(range(1, R*C-2) + [R*C-1, R*C-2, 0])
        expected = {(C*i+j+1) % (R*C) : (i, j)
                    for i in xrange(R) for j in xrange(C)}

        min_heap = [(0, 0, begin.index(0), begin)]
        lookup = {begin: 0}
        while min_heap:
            f, g, zero, board = heapq.heappop(min_heap)
            if board == end: return g
            if board == end_wrong: return -1
            if f > lookup[board]: continue

            r, c = divmod(zero, C)
            for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i, j = r+direction[0], c+direction[1]
                if 0 <= i < R and 0 <= j < C:
                    new_zero = C*i+j
                    tmp = list(board)
                    tmp[zero], tmp[new_zero] = tmp[new_zero], tmp[zero]
                    new_board = tuple(tmp)
                    f = g+1+heuristic_estimate(new_board, R, C, expected)
                    if f < lookup.get(new_board, float("inf")):
                        lookup[new_board] = f
                        heapq.heappush(min_heap, (f, g+1, new_zero, new_board))
        return -1


print(Solution().slidingPuzzle([[1,2,3],[4,0,5]])) # 1
print(Solution().slidingPuzzle([[1,2,3],[5,4,0]])) # -1
print(Solution().slidingPuzzle([[4,1,2],[5,0,3]])) # 5
print(Solution().slidingPuzzle([[3,2,4],[1,5,0]])) # 14