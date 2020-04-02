# Time:  O(log(min(x, y))) 取决于计算最大公约数所使用的辗转相除法
# Space: O(1)

# 365
# You are given two jugs with capacities x and y litres.
# There is an infinite amount of water supply available.
# You need to determine whether it is possible to
# measure exactly z litres using these two jugs.
#
# Operations allowed:
#
# - Fill any of the jugs completely.
# - Empty any of the jugs.
# - Pour water from one jug into another till the other jug is completely full or
# the first jug itself is empty.
# Example 1:
#
# Input: x = 2, y = 6, z = 4
# Output: True
# Example 2:
#
# Input: x = 2, y = 6, z = 5
# Output: False

# Bézout's identity (also called Bézout's lemma): Let a and b be integers with greatest common divisor d. Then,
# there exist integers x and y such that ax + by = d. More generally, the integers of the form ax + by are
# exactly the multiples of d.
#
# ax+by=z 有解当且仅当 z 是 x,y 的最大公约数的倍数。因此我们只需要找到 x,y
# 的最大公约数并判断 z是否是它的倍数即可。
#
# Note 每次操作只会让桶里的水总量增加 x，增加 y，减少 x，或者减少 y。
# 你可能认为这有问题：如果往一个不满的桶里放水，或者把它排空呢？那变化量不就不是 x 或者 y 了吗？接下来我们来解释这一点：
# 首先要清楚，在题目所给的操作下，两个桶不可能同时有水且不满。因为观察所有题目中的操作，操作的结果都至少有一个桶是空的或者满的；
#
# 其次，对一个不满的桶加水是没有意义的。因为如果另一个桶是空的，那么这个操作的结果等价于直接从初始状态给这个桶加满水；而如果另一个桶是满的，
# 那么这个操作的结果等价于从初始状态分别给两个桶加满；
# 再次，把一个不满的桶里面的水倒掉是没有意义的。因为如果另一个桶是空的，那么这个操作的结果等价于回到初始状态；而如果另一个桶是满的，
# 那么这个操作的结果等价于从初始状态直接给另一个桶倒满。
#
# 因此，我们可以认为每次操作只会给水的总量带来 x 或者 y 的变化量。因此我们的目标可以改写成：找到一对整数a,b，使得ax+by=z
#
# 而只要满足z≤x+y，且这样的a,b 存在，那么我们的目标就是可以达成的。这是因为：
#
# 若 a≥0,b≥0，那么显然可以达成目标。
# 若 a<0(b<0同样方法)，那么可以进行以下操作：
# 1 往 y 壶倒水；
# 2 把 y 壶的水倒入 x 壶；
# 3 如果 y 壶不为空，那么 x 壶肯定是满的，把 x 壶倒空，然后再把 y 壶的水倒入 x 壶。
# 重复以上操作直至某一步时 x 壶进行了 a 次倒空操作，y 壶进行了 b 次倒水操作。 E.g x=3,y=5, we have (-2)*3 + 2*5 = 4
# 加满b水壶2次，加满并倒掉a水壶2次->b水壶剩余水量4.

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # math.gcd(5,0) -> 5, math.gcd(0,5) -> 5. Function below works too, no divide-by-zero error.
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        # The problem is to solve:
        # - check z <= x + y
        # - check if there is any (a, b) integers s.t. ax + by = z
        return z == 0 or ((z <= x + y) and (z % gcd(x, y) == 0))

# DFS
# Time:  O(xy) 状态数最多有(x+1)(y+1)种，对每一种状态进行深度优先搜索的时间复杂度为O(1)，因此总时间复杂度为 O(xy)
# Space: O(xy) 状态数最多有(x+1)(y+1)种，哈希集合中最多会有(x+1)(y+1)项，因此空间复杂度为O(xy)

# 这一类游戏相关的问题，用人脑去想，是很难穷尽所有的可能情况的。因此很多时候需要用到「搜索算法」。
# 搜索算法一般是在「树」或者「图」结构上的深度优先遍历或者广度优先遍历。因此，在脑子里，更建议动手在纸上画出问题抽象出来的「树」或者「图」的样子。
#
# 在「树」上的「深度优先遍历」就是「回溯算法」，在「图」上的「深度优先遍历」是「flood fill」 算法，深搜比较节约空间。
# 广搜一层一层像水波纹一样扩散，路径最短。所谓状态，就是指当前的任务进行到哪个阶段了，可用变量来表示。本题用一个有序整数对表示两水壶水量。
# 从当前状态最多可以进行 8 种操作，得到8个新状态。因为状态有重复，因此是一个「有向」且「有环」的图，在遍历的时候，需要判断该结点设置是否访问过.

# 首先建模。观察题目可知，在任意一个时刻，此问题的状态可以由两个数字决定：X 壶中的水量，以及 Y 壶中的水量。
# 在任意一个时刻，我们可以且仅可以采取以下几种操作：
# 把 X 壶灌满；
# 把 Y 壶灌满；
# 把 X 壶倒空；
# 把 Y 壶倒空；
# 把 X 壶的水灌进 Y 壶，直至灌满或倒空；
# 把 Y 壶的水灌进 X 壶，直至灌满或倒空。

# 因此，可以使用深度优先搜索来解决。搜索中的每一步以 remain_x, remain_y 作为状态，即X壶和Y壶中的水量。在每一步搜索时，
# 依次尝试所有的操作，递归搜索。这可能会导致我们陷入无止境的递归，因此需要使用一个哈希存储所有已经搜索过的remain_x, remain_y状态，
# 保证每个状态至多只被搜索一次。
#
# 在实际的代码编写中，由于深度优先搜索导致的递归远远超过了 Python 的默认递归层数（可以使用 sys 库更改递归层数，但不推荐这么做），
# 因此下面的代码使用栈来模拟递归，避免了真正使用递归而导致的问题。
class Solution_dfs(object):
    def canMeasureWater_recurDepth(self, x, y, z):
        def dfs(remain_x, remain_y):
            if remain_x == z or remain_y == z or remain_x+remain_y == z:
                return True
            if (remain_x, remain_y) not in seen:
                seen.add((remain_x, remain_y))
                if dfs(x, remain_y): return True # 把 X 壶灌满
                if dfs(remain_x, y): return True # 把 Y 壶灌满
                if dfs(0, remain_y): return True # 把 X 壶倒空
                if dfs(remain_x, 0): return True # 把 Y 壶倒空
                # 把 X 壶的水灌进 Y 壶，直至灌满或倒空
                delta = min(remain_x, y - remain_y)
                if dfs(remain_x - delta, remain_y + delta): return True
                # 把 Y 壶的水灌进 X 壶，直至灌满或倒空
                delta = min(remain_y, x - remain_x)
                if dfs(remain_x + delta, remain_y - delta): return True
            return False

        seen = set()
        return dfs(0, 0)

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))

            stack.append((x, remain_y)) # 把 X 壶灌满
            stack.append((remain_x, y)) # 把 Y 壶灌满
            stack.append((0, remain_y)) # 把 X 壶倒空
            stack.append((remain_x, 0)) # 把 Y 壶倒空
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False

print(Solution().canMeasureWater(3,5,4)) # True
print(Solution().canMeasureWater(2,6,5)) # False
print(Solution().canMeasureWater(0,5,5)) # True
print(Solution().canMeasureWater(5,0,5)) # True
print(Solution().canMeasureWater(0,0,5)) # False
