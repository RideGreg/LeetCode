# Time:  O(n)
# Space: O(n)

# 1042
# You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.
#
# paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
#
# Also, there is no garden that has more than 3 paths coming into or leaving it.
#
# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path,
# they have different types of flowers.
#
# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.
# The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        result = [0]*N
        G = [[] for _ in range(N)]
        for x, y in paths:
            x, y = min(x,y), max(x,y)
            #G[x-1].append(y-1) # only need to check the smaller gardens which are already assigned flowers
            G[y-1].append(x-1)
        for i in range(N):
            result[i] = ({1, 2, 3, 4} - {result[j] for j in G[i]}).pop()
        return result

    # maintain 'avoid' dict for flowers already used by neighbors.
    # we know the size of nei and avoid, so not need to use collections.defaultdict(list)
    # actually, 'avoid' is not needed (can check ans instead)
    def gardenNoAdj_ming(self, N: int, paths: List[List[int]]) -> List[int]:
        nei, avoid = [[] for _ in range(N)], [set() for _ in range(N)]
        ans = [0]*N
        for x, y in paths:
            x, y = min(x,y), max(x,y)
            nei[x-1].append(y-1)
        for i in range(N):
            for c in [1,2,3,4]:
                if c not in avoid[i]:
                    ans[i] = c
                    for ne in nei[i]:
                        avoid[ne].add(c)
                    break
        return ans