# Time:  O(2^n) 每个数字最多有两种选择
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
    def numsSameConsecDiff(self, N, K): # USE THIS: BFS, kamyu
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        curr = list(range(10))
        for _ in range(N-1):
            curr = [x*10 + y
                    for x in curr for y in set([x%10 + K, x%10 - K]) 
                    if x > 0 and 0 <= y < 10]
        return curr


    def numsSameConsecDiff_dfs(self, N, K):
        def dfs(sz, num):
            if sz == N:
                ans.append(num)
                return

            if sz == 0:
                cand = range(1, 10)
            else:
                d = num % 10
                cand = set([d+K, d-K])  # NOTE! remove dup for K=0
            for v in cand:
                if 0<=v<10:
                    dfs(sz+1, num*10+v)
                

        ans = []
        dfs(0, 0)
        if N == 1: ans.append(0)
        return ans



print(Solution().numsSameConsecDiff(3, 7)) # [181,292,707,818,929]
print(Solution().numsSameConsecDiff(2, 1)) # [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]