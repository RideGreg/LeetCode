# Time:  O(n * n!) we have n! results, each need n step to genrate. 
# Space: O(n) recursion depth

# 47
# Given a collection of DISTINCT numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers

    # Backtrack: all positions share the same candidates, so maintain a 'used' list.
    # list is more space-efficient than set (set requires space overhead for quick membership tests)
    # https://stackoverflow.com/questions/13547883/is-python-set-more-space-efficient-than-list
    def permute(self, num): #  USE THIS
        def backtrack(cur):
            if len(cur) == len(num):
                result.append(cur[:])
                return
            for i in range(len(num)):
                if not used[i]:
                    used[i] = True
                    cur.append(num[i])
                    backtrack(cur)
                    cur.pop()
                    used[i] = False

        result = []
        used = [False] * len(num)
        backtrack([])
        return result


    # iteration: this method cannot guarantee the result is in sorted order
    def permute2(self, num): # insert each new number to all possible positions
        ans = [[]]
        for n in num:
            nxt = []
            for p in ans:   # O(n!)
                for i in range(len(p)+1):  # O(n)
                    nxt.append(p[:i]+[n]+p[i:])
            ans = nxt
        return ans


    # NOT USE: simulation: switch each number to the end, then end-1.. end-2..
    def permute3(self, num):
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