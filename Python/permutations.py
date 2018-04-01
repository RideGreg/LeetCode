# Time:  O(n * n!) Ming: should be O(n!)?
# Space: O(n)
#
# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#

# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        used = [False] * len(num)
        self.permuteRecu(result, used, [], num)
        return result

    def permuteRecu(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur[:])
            return
        for i in xrange(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.permuteRecu(result, used, cur, num)
                cur.pop()
                used[i] = False

    def permute_iterative(self, num):
        ans = [[]]
        for n in nums:
            new = []
            for p in ans:
                for i in xrange(len(p)+1):
                    new.append(p[:i]+[n]+p[i:])
            ans = new
        return ans
if __name__ == "__main__":
    print len(Solution().permute([1, 2, 3]))

class Solution2:
    def permute(self, num):
        def helper(ans, n, arrangement):
            if n <= 0:
                ans.append(arrangement+[])
                return

            for i in xrange(n):
                arrangement[i], arrangement[n - 1] = arrangement[n - 1], arrangement[i]
                helper(ans, n - 1, arrangement)
                arrangement[i], arrangement[n - 1] = arrangement[n - 1], arrangement[i]

        ans = []
        helper(ans, len(num), num)
        return ans

import time
if __name__ == "__main__":
    t = time.time()
    for _ in xrange(1000):
        print Solution().permute([1, 2, 3])
        print Solution().permute([1, 2, 3, 4])
    print time.time()-t, 'seconds'

