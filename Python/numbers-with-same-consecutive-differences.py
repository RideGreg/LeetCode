# Time:  O(2^n)
# Space: O(2^n)

# 967
# Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
#
# Note that every number in the answer must not have leading zeros except for the number 0 itself. For example,
# 01 has one leading zero and is invalid, but 0 is valid.
#
# You may return the answer in any order.

# 1 <= N <= 9
# 0 <= K <= 9

class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        def dfs(cur, N, K):
            if len(str(cur)) == N:
                ans.append(cur)
                return

            last = cur % 10
            for d in set([last + K, last - K]):
                if 0 <= d <= 9:
                    dfs(cur * 10 + d, N, K)

        ans = []
        for i in xrange([0, 1][N > 1], 10):
            dfs(i, N, K)
        return ans

    def numsSameConsecDiff_kamyu(self, N, K):
        curr = range(10)
        for i in xrange(N-1):
            curr = [x*10 + y for x in curr for y in set([x%10 + K, x%10 - K]) 
                    if x and 0 <= y < 10]
        return curr

print(Solution().numsSameConsecDiff(3, 7)) # [181,292,707,818,929]
print(Solution().numsSameConsecDiff(2, 1)) # [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]