# Time:  O(nlogn)
# Space: O(1)

# 1288 biweekly contest 15 12/14/2019
#
# Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b)
# is covered by interval [c,d) if and only if c <= a and b <= d.
#
# After doing so, return the number of remaining intervals.
#
# Constraints:
#
#     1 <= intervals.length <= 1000
#     0 <= intervals[i][0] < intervals[i][1] <= 10^5
#     intervals[i] != intervals[j] for all i != j

class Solution(object):
    def removeCoveredIntervals(self, intervals):  # USE THIS
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        #intervals.sort() # KENG: this is WRONG for [[1,4],[1,6]]
        intervals.sort(key = lambda x: (x[0], -x[1]))
        ly = intervals[0][1]
        ans = 1
        for _, y in intervals[1:]:
            if y > ly:
                ly = y
                ans += 1
        return ans

    def removeCoveredIntervals_kamyu(self, intervals):
        intervals.sort(key=lambda x: [x[0], -x[1]])
        result, max_right = 0, 0
        for left, right in intervals:
            result += int(right > max_right)
            max_right = max(max_right, right)
        return result

print(Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]])) # 2
print(Solution().removeCoveredIntervals([[1,4],[1,6]])) # 1
