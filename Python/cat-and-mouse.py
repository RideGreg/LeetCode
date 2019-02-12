# Time:  O(n^3)
# Space: O(n^2)

# 913
# A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.
#
# The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.
#
# Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.
#
# During each player's turn, they must travel along one edge of the graph that meets where they are.
# For example, if the Mouse is at node 1, it must travel to any node in graph[1].
#
# Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)
#
# Then, the game can end in 3 ways:
#
# If ever the Cat occupies the same node as the Mouse, the Cat wins.
# If ever the Mouse reaches the Hole, the Mouse wins.
# If ever a position is repeated
# (ie. the players are in the same position as a previous turn,
# and it is the same player's turn to move), the game is a draw.
# Given a graph, and assuming both players play optimally,
# return 1 if the game is won by Mouse, 2 if the game is won by Cat, and 0 if the game is a draw.
#
# Example 1:
#
# Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# Output: 0
# Explanation:
# 4---3---1
# |   |
# 2---5
#  \ /
#   0
#
# Note:
# - 3 <= graph.length <= 50
# - It is guaranteed that graph[1] is non-empty.
# - It is guaranteed that graph[2] contains a non-zero element. 

import collections

# Intuition: The state of the game can be represented as (m, c, t) where m, c are the locations of mouse and cat, and
# t represents whose turn to move (1 for mouse's move, 2 for cat's move). Let's call these states nodes. These states
# form a directed graph: the player whose turn it is has various moves considered as outgoing edges from this node to other nodes.
#
# Some of these nodes are already resolved: if the mouse is at the hole (m = 0), then the mouse wins; if the cat is
# where the mouse is (c = m), then the cat wins. Let's say that nodes will either be colored MOUSE, CAT, or DRAW
# depending on which player is assured victory.
#
# As in a standard minimax algorithm, the Mouse player will prefer MOUSE nodes first, DRAW nodes second, and
# CAT nodes last, and the Cat player prefers these nodes in the opposite order.
#
# Algorithm
# We will color each node marked DRAW according to the following rule. (We'll suppose the node has node.turn = Mouse: the other case is similar.)
#
# ("Immediate coloring"): If there is a child that is colored MOUSE, then this node will also be colored MOUSE.
# ("Eventual coloring"): If all children are colored CAT, then this node will also be colored CAT.
#
# We repeatedly do this kind of coloring until no node satisfies the above conditions. To perform this coloring
# efficiently, we will use a queue and perform a bottom-up percolation:
#
# 1. Enqueue any node initially colored (where the Mouse is at the Hole, or the Cat is at the Mouse.)
#
# 2. For every node in the queue, for each parent of that node:
# Do an immediate coloring of parent if you can.
# If you can't, then decrement the side-count of the number of children marked DRAW. If it becomes zero, then do an
# "eventual coloring" of this parent.
#
# 3. All parents that were colored in this manner get enqueued to the queue.

class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)

        # What nodes could play their turn to arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2: # now cat's move, so the last move is mouse
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in xrange(N):
            for c in xrange(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c]) # cat cannot goes to 0 Hole

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in xrange(N):
            for t in xrange(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            i, j, t, c = queue.popleft() # for nodes that are colored
            for i2, j2, t2 in parents(i, j, t): # for every parent of this node i, j, t
                if color[i2, j2, t2] is DRAW: # if this parent is not colored
                    # if the parent can make a winning move (ie. mouse move to MOUSE, and cat move to CAT)
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]

    # kamyu solution has a bug for 2nd testcase [[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]
    # it returns 0, while actually optimal path for mouse returns 1.th
    # The bug is because lookup[(9,5,False)] was set as 0/draw in non-optimal path and optimal path never has a chance
    # to run. This problem has cyclic edges, while the classical tree-shape minimax problem has only one way flow.
    def catMouseGame_kamyu(self, graph):
        HOLE, MOUSE_START, CAT_START = range(3)
        DRAW, MOUSE, CAT = range(3)

        def move(lookup, i, other_i, is_mouse_turn):
            key = (i, other_i, is_mouse_turn)
            if key in lookup:
                return lookup[key]

            lookup[key] = DRAW
            if is_mouse_turn:
                skip, target, win, lose = other_i, HOLE, MOUSE, CAT
            else:
                skip, target, win, lose = HOLE, other_i, CAT, MOUSE                
            for nei in graph[i]:
                if nei == target:
                    result = win
                    break
            else:
                result = lose
                for nei in graph[i]:
                    if nei == skip:
                        continue
                    tmp = move(lookup, other_i, nei, not is_mouse_turn)
                    if tmp == win:
                        result = win
                        break
                    if tmp == DRAW:
                        result = DRAW
            lookup[key] = result
            return result

        return move({}, MOUSE_START, CAT_START, True)

print(Solution().catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]])) # 0
# 4---3---1
# |   |
# 2---5
#  \ /
#   0
print(Solution().catMouseGame([[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]])) # 1
# 1--4--5--6--10--7--9--2
#       |  |      |
#       3  0      8
