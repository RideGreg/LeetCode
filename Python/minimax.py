# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/

# Consider a game which has 4 final states and paths to reach final state are from root to 4 leaves of a perfect binary tree.
# Assume you are the maximizing player and you get the first chance to move, i.e., you are at the root and your opponent
# at next level who tries to minimizing the score at final state. Assume both maximizer and minimizer plays optimally.
# Find maximum score that maximizing player can get. And min score the minimizer can get.

import math


def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # base case : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 2, False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 2, True, scores, targetDepth))


# Driver code
#      3
#   5      2
# 9  12  5  23
scores = [3, 5, 2, 9, 12, 5, 23]

treeDepth = math.floor(math.log(len(scores), 2))

print("The optimal value for maximizer is : ")
print(minimax(0, 0, True, scores, treeDepth)) # 9
print("The optimal value for minimizer is : ")
print(minimax(0, 0, False, scores, treeDepth)) # 12