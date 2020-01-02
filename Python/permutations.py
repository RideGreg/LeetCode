# Time:  O(n * n!)
# Space: O(n)

# 47
# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#

class Solution:
    def permute(self, num): # USE THIS: insert each new number to all possible positions
        ans = [[]]
        for n in num:
            nxt = []
            for p in ans:   # O(n!)
                for i in range(len(p)+1):  # O(n)
                    nxt.append(p[:i]+[n]+p[i:])
            ans = nxt
        return ans

class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        used = [False] * len(num)
        self.dfs(result, used, [], num)
        return result

    def dfs(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur[:])
            return
        for i in range(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.dfs(result, used, cur, num)
                cur.pop()
                used[i] = False



class Solution3:   # NOT USE: simulation: switch each number to the end, then end-1.. end-2..
    def permute(self, num):
        def helper(ans, n, arrangement):
            if n <= 0:
                ans.append(arrangement+[])
                return

            for i in range(n):
                arrangement[i], arrangement[n - 1] = arrangement[n - 1], arrangement[i]
                helper(ans, n - 1, arrangement)
                arrangement[i], arrangement[n - 1] = arrangement[n - 1], arrangement[i]

        ans = []
        helper(ans, len(num), num)
        return ans

print(Solution().permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

