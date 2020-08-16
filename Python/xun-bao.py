# Assume maze area s, # of buttons is m, # of stones is o
# Time:  O(ms + m^2*o + 2^m * m^2), m BFS is O(ms)， pre-process the shortest distance of any 2 buttons 
#      through a stone is O(m^2*o), DP is O(2^m * m^2)
# Space: O(s + bs + 2^m*m), BFS queue needs O(s), pre-process the shortest distance from M_i to 
#      any point needs O(bs), DP needs O(2^m*m)


# LCP 13
# 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。
# 迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。
# 但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。
#
# 要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。
# 但是由于石头太重，我们一次只能搬一个石头到指定地点。

# 迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、
# 起点和终点（无论是否能拿到宝藏）也是可以通行的。

# 我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，
# 我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。
# 1 <= maze.length <= 100
# 1 <= maze[i].length <= 100
# maze[i].length == maze[j].length
# S 和 T 有且只有一个
# 0 <= M的数量 <= 16
# 0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。


# Solution BFS+DP+状态压缩:
# 实际上的走法只有几种： 从 S 走到 O，从 O 走到 M，从 M 走到 O，从 M 走到 T
# 1. maze中，每个位置到地图上任意的其他位置的距离是不会变化的，因此使用BFS算法计算并保存（题解中实际上只计算了起点到任意点的距离以及每个机关i到任意点的距离）
# - 在最开始，我们一定会从 S，经过某一个 O，到达某一个 M。那么对于特定的 M 来说，我们枚举 O 就可以计算 S−O−M 的最短距离。
# - 假定我们已经从起点到达了某个 M 了，接下来需要去其他的 O 点搬石头接着触发其他的机关，这是一个 M-O-M'的路线。同样的道理，对于给定 M 和 M'，可以枚举确定一个 O，使得 M-O-M'距离最短。

# 需要所有的 M 都被触发，M 的触发顺序不同会导致行走的路径长度不同。这里一共有16 个 M，我们用d(i,j) 表示第 i 个 M 到第 j 个 M 经过某一个 O 的最短距离。
# 使用一个 16 位的二进制数表示状态
# 2. 使用dist数组，记录机关i到机关j的最短距离，从机关i到机关j需要经过一次石头，因此每计算一个dist[i][j]都需要遍历所有的石头

# 3. 状态压缩的dp，利用二进制的mask来保存当前的状态，dp[mask][j]表示当前处于第j个机关，
# 总的触发状态为mask所需要的最短路径。由于有nb个机关，每个机关都有访问和未访问两种状态，共有2**nb个状态，因此(1<<nb)*nb的空间开销已经必不可少了
# 4. 最后，所有状态都被访问以后，还应当从最后一个状态j出发，前往终点，最终比较得到最短的距离

# 边界情况较多，比如迷宫没有 M、M不可达等。

# 题型小结
# 这道题是一个非常经典的状态压缩动态规划模型：有 n个任务 {M_1, M_2 ... M_n }，每两个任务之间有一个 c(M_i, M_j)表示在 M_i之后（下一个）做 M_j的花费，
# 让你求解把 n 个任务都做完需要的最小花费。通常这个 n 会非常的小，因为需要构造 2^n种状态，
# c(M_i, M_j)可能是题目给出，也可能是可以在很短的时间内计算出来的一个值。这类问题的状态设计一般都是 f(mask,i) 表示当前任务完成的状态是mask，当前位置是 i，
# 考虑转移的时候我们只需要考虑当前任务的上一个任务即可。希望读者可以理解这里的思想，并尝试使用记忆化搜索和循环两种方式实现。


from typing import List
import collections

class Solution(object):
    def minimalSteps(self, maze: List[str]) -> int:
        dd = [(-1,0), (1,0), (0,-1), (0,1)]

        # 计算（x, y）到maze中其他点的距离，结果保存在ret中
        def bfs(x, y, m, n):
            ret = [[-1]*n for _ in range(m)]
            ret[x][y] = 0
            q = collections.deque([(x, y)])
            while q:
                curx, cury = q.popleft()
                for dx, dy in dd:
                    nx = curx + dx
                    ny = cury + dy
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != '#' and ret[nx][ny] == -1:
                        ret[nx][ny] = ret[curx][cury] + 1
                        q.append((nx, ny))
            return ret

        m, n = len(maze), len(maze[0])
        startX = startY = endX = endY = -1
        # 机关 & 石头
        buttons, stones = [], []

        # 记录所有特殊信息的位置
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    startX, startY = i, j
                elif maze[i][j] == 'T':
                    endX, endY = i, j
                elif maze[i][j] == 'O':
                    stones.append((i,j))
                elif maze[i][j] == 'M':
                    buttons.append((i,j))
        
        nb, ns = len(buttons), len(stones)

        startToAnyPos = bfs(startX, startY, m, n)

        # 若没有机关，最短距离就是(startX, startY)到(endX, endY)的距离
        if nb == 0:
            return startToAnyPos[endX][endY]

        # 记录第i个机关到第j个机关的最短距离
        # dist[i][nb]表示到起点的距离， dist[i][nb+1]表示到终点的距离
        dist = [[-1]*(nb+2) for _ in range(nb)]

        # 遍历所有机关，计算其和其他点的距离
        buttonsToAnyPos = []
        for i in range(nb):
            bx, by = buttons[i]
            # 记录第i个机关到其他点的距离
            iToAnyPos = bfs(bx, by, m, n)
            buttonsToAnyPos.append(iToAnyPos)
            # 第i个机关到终点的距离就是(bx, by)到(endX, endY)的距离
            dist[i][nb + 1] = iToAnyPos[endX][endY]
        
        for i in range(nb):
            # 计算第i个机关到(startX, startY)的距离
            # 即从第i个机关出发，通过每个石头(sx, sy)，到(startX, startY)的最短距离
            tmp = -1
            for j in range(ns):
                sx, sy = stones[j]
                if buttonsToAnyPos[i][sx][sy] != -1 and startToAnyPos[sx][sy] != -1:
                    if tmp == -1 or tmp > buttonsToAnyPos[i][sx][sy] + startToAnyPos[sx][sy]:
                        tmp = buttonsToAnyPos[i][sx][sy] + startToAnyPos[sx][sy]

            dist[i][nb] = tmp

            # 计算第i个机关到第j个机关的距离
            # 即从第i个机关出发，通过每个石头(sx, sy)，到第j个机关的最短距离
            for j in range(i+1, nb):
                mn = -1
                for k in range(ns):
                    sx, sy = stones[k]
                    if buttonsToAnyPos[i][sx][sy] != -1 and buttonsToAnyPos[j][sx][sy] != -1:
                        if mn == -1 or mn > buttonsToAnyPos[i][sx][sy] + buttonsToAnyPos[j][sx][sy]:
                            mn = buttonsToAnyPos[i][sx][sy] + buttonsToAnyPos[j][sx][sy]
                # 距离是无向图，对称的
                dist[i][j] = mn
                dist[j][i] = mn
        
        # 若有任意一个机关 到起点或终点没有路径(即为-1),则说明无法达成，返回-1
        if any(dist[i][nb] == -1 or dist[i][nb+1] == -1 for i in range(nb)):
            return -1
        
        # dp数组， -1代表没有遍历到, 1<<nb表示题解中提到的mask, dp[mask][j]表示当前处于第j个机关，总的触发状态为mask所需要的最短路径, 由于有2**nb个状态，因此1<<nb的开销必不可少
        dp = [[-1]*nb for _ in range(1 << nb)]
        # 初识状态，即从start到第i个机关，此时mask的第i位为1，其余位为0
        for i in range(nb):
            dp[1 << i][i] = dist[i][nb]
        
        # 二进制中数字大的mask的状态肯定比数字小的mask的状态多，所以直接从小到大遍历更新即可
        for mask in range(1, (1 << nb)):
            for i in range(nb):
                # 若当前位置是正确的，即mask的第i位是1
                if mask & (1 << i) != 0:
                    for j in range(nb):
                        # 选择下一个机关j,要使得机关j目前没有到达，即mask的第j位是0
                        if mask & (1 << j) == 0:
                            nextMask = mask | (1 << j)
                            if dp[nextMask][j] == -1 or dp[nextMask][j] > dp[mask][i] + dist[i][j]:
                                dp[nextMask][j] = dp[mask][i] + dist[i][j]

        # 最后一个机关到终点
        ans = -1
        finalMask = (1 << nb) - 1
        for i in range(nb):
            if ans == -1 or ans > dp[finalMask][i] + dist[i][nb + 1]:
                ans = dp[finalMask][i] + dist[i][nb + 1]
        return ans


print(Solution().minimalSteps(["S#O", "M..", "M.T"])) # 16
print(Solution().minimalSteps(["S#O", "M.#", "M.T"])) # -1
print(Solution().minimalSteps(["S#O", "M.T", "M.."])) # 17