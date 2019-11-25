# Time:  O(n^2) = O(1), since n is at most 99
# Space: O(n) = O(1)

# 799
# We stack glasses in a pyramid, where the first row has 1 glass,
# the second row has 2 glasses, and so on until the 100th row.
# Each glass holds one cup (250ml) of champagne.
#
# Then, some champagne is poured in the first glass at the top.
# When the top most glass is full, any excess liquid poured will fall
# equally to the glass immediately to the left and right of it.
# When those glasses become full, any excess champagne will fall
# equally to the left and right of those glasses, and so on.
# (A glass at the bottom row has it's excess champagne fall on the floor.)
#
# For example, after one cup of champagne is poured, the top most glass is full.
# After two cups of champagne are poured, the two glasses on the second row are half full.
# After three cups of champagne are poured, those two cups become full -
# there are 3 full glasses total now.  After four cups of champagne are poured,
# the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
#
# Now after pouring some non-negative integer cups of champagne,
# return how full the j-th glass in the i-th row is (both i and j are 0 indexed.)
#
# Example 1:
# Input: poured = 1, query_glass = 1, query_row = 1
# Output: 0.0
# Explanation: We poured 1 cup of champange to the top glass of the tower
#  (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
#
# Example 2:
# Input: poured = 2, query_glass = 1, query_row = 1
# Output: 0.5
# Explanation: We poured 2 cups of champange to the top glass of the tower
# (which is indexed as (0, 0)). There is one cup of excess liquid.
# The glass indexed as (1, 0) and the glass indexed as (1, 1) will share
# the excess liquid equally, and each will get half cup of champange.
#
# Note:
# - poured will be in the range of [0, 10 ^ 9].
# - query_glass and query_row will be in the range of [0, 99].

class Solution(object):
    # Simulation: keep track of the total amount of champagne that flows through a glass.
    def champagneTower(self, poured, query_row, query_glass): # USE THIS
        dp = [poured]
        for i in range(1, query_row + 1):
            ndp = [0.0] * (i+1)
            for j in range(len(dp)):
                if dp[j] > 1.0:
                    v = (dp[j] - 1.0) / 2
                    ndp[j] += v
                    ndp[j+1] += v
            dp = ndp
        return min(1.0, dp[query_glass])
        ''' full space DP
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = poured
        for r in range(query_row):
            for c in range(r + 1):
                q = (dp[r][c] - 1) / 2.0
                if q > 0:
                    dp[r + 1][c] += q
                    dp[r + 1][c + 1] += q

        return min(1.0, dp[query_row][query_glass])
        '''

    def champagneTower_kamyu(self, poured, query_row, query_glass): # 1-D space is hard to understand
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        result = [poured] + [0.0] * query_row
        for i in range(1, query_row+1):
            for j in reversed(range(i+1)):
                print(j, result)
                result[j] = max(result[j]-1, 0)/2.0 + \
                            max(result[j-1]-1, 0)/2.0
                print(result)
        return min(result[query_glass], 1.0)

    def champagneTower_ming(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[poured]]
        # KENG: only need to calculate required rows, otherwise LTE sicne poured can be huge
        while len(dp) < query_row + 1 and any(x > 1.0 for x in dp[-1]):
            nr = [0.0] * (len(dp)+1)
            for i in range(len(dp[-1])):
                if dp[-1][i] > 1.0:
                    v = (dp[-1][i] - 1.0) / 2
                    nr[i] += v
                    nr[i+1] += v
                    dp[-1][i] = 1.0 # this is not necessary, return will do min(1.0....)
            dp.append(nr)
        if query_row >= len(dp) or query_glass >= len(dp[query_row]):
            return 0.0
        else:
            return min(1.0, dp[query_row][query_glass])

print(Solution().champagneTower(4,2,0)) # 0.25
print(Solution().champagneTower(10**9, 99, 99)) # 0.0
print(Solution().champagneTower(10**9, 99, 50)) # 1.0