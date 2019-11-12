# Time:  O(n^2 * k)
# Space: O(n)

# 568
# LeetCode wants to give one of its best employees the option to travel among N cities to collect
# algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations
# in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of
# vacation days you could take, but there are certain rules and restrictions you need to follow.
#
# Rules and restrictions:
# 1. You can only travel among N cities, represented by indexes from 0 to N-1. Initially,
# you are in the city indexed 0 on Monday.
# 2. The cities are connected by flights. The flights are represented as a N*N matrix (not necessary
# symmetrical), called flights representing the airline status from the city i to the city j.
# If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1.
# Also, flights[i][i] = 0 for all i.
# 3. You totally have K weeks (each week has 7 days) to travel. You can only take flights at most
# once per day and can only take flights on each week's Monday morning. Since flight time is so short,
# we don't consider the impact of flight time.
# 4. For each city, you can only have restricted vacation days in different weeks, given an N*K matrix
# called days representing this relationship. For the value of days[i][j], it represents the maximum
# days you could take vacation in the city i in the week j.

# You're given the flights matrix and days matrix, and you need to output the maximum vacation days
# you could take during K weeks.

# Note:
# 1 N and K are positive integers, which are in the range of [1, 100].
# 2 In the matrix flights, all the values are integers in the range of [0, 1].
# 3 In the matrix days, all the values are integers in the range [0, 7].
# 4 You could stay at a city beyond the number of vacation days, but you should work on the extra days,
# which won't be counted as vacation days.
# 5 If you fly from the city A to the city B and take the vacation on that day, the deduction towards
# vacation days will count towards the vacation days of city B in that week.
# 6 We don't consider the impact of flight hours towards the calculation of vacation days.



# Solution: DP
# dp[w][c]表示第w周选择留在第c个城市可以获得的最大总收益
#
# 初始令dp[w][0] = 0, dp[w][1 .. c - 1] = -1
#
# 当dp[w][c] < 0时，表示第c个城市在第w周时还不可达。
#
# 状态转移方程：
# for w in (0 .. K)
#     for sc in (0 .. N)
#         if dp[w][sc] < 0:
#             continue
#         for tc in (0 .. N)
#             if sc == tc or flights[sc][tc] == 1:
#                 dp[w + 1][tc] = max(dp[w + 1][tc], dp[w][sc] + days[tc][w])

class Solution(object):
    def maxVacationDays(self, flights, days): # USE THIS
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        N, K = len(days), len(days[0])
        dp = [0] + [-1]* (N-1)
        for k in range(K):
            ndp = [-1] * N
            for sc in range(N):
                if dp[sc] == -1: continue
                for tc in range(N):
                    if sc == tc or flights[sc][tc]:
                        ndp[tc] = max(ndp[tc], dp[sc]+days[tc][k])
            dp = ndp
        return max(dp)

    def maxVacationDays_kamyu(self, flights, days):
        if not days or not flights:
            return 0
        dp = [[0] * len(days) for _ in xrange(2)]
        for week in reversed(xrange(len(days[0]))):
            for cur_city in xrange(len(days)):
                dp[week % 2][cur_city] = days[cur_city][week] + dp[(week+1) % 2][cur_city]
                for dest_city in xrange(len(days)):
                    if flights[cur_city][dest_city] == 1:
                        dp[week % 2][cur_city] = max(dp[week % 2][cur_city], \
                                                     days[dest_city][week] + dp[(week+1) % 2][dest_city])
        return dp[0][0]


print(Solution().maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], [[1,3,1],[6,0,3],[3,3,3]])) # 12
print(Solution().maxVacationDays([[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[7,7,7],[7,7,7]])) # 3
print(Solution().maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], [[7,0,0],[0,7,0],[0,0,7]])) # 21
