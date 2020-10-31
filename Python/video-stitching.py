# Time:  O(nlogn)
# Space: O(1)

# 1024
# You are given a series of video clips from a sporting event that lasted T seconds.  These video clips
# can be overlapping with each other and have varied lengths.
#
# Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].
# We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments
# [0, 1] + [1, 3] + [3, 7].
#
# Return the minimum number of clips needed so that we can cut the clips into segments that cover
# the entire sporting event ([0, T]).  If the task is impossible, return -1.

from typing import List

class Solution(object):
    # 1. Greedy: only introduce new segment when necessary
    # 2. Similar to Interval Merge problem
    # 2. Interval problem: most likely need sort: sort by left end, use maximum right end
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        # ans 初始化为1而不是0，不然无法处理第一段就满足条件的情况，因为后面代码只有在出现断口才会increment ans
        # curend 上一个segment能cover到哪儿，tmpend 当前遍历的新的segment能续到哪儿
        # tmpend永远大于等于curend
        ans, curend, tmpend = 1, 0, 0
        clips.sort()
        for left, right in clips:
            if left > curend:   # no longer covered by curend, has to introduce a new segment
                if left > tmpend:
                    return -1
                curend, ans = tmpend, ans + 1

            # if still less than curend, don't update curend/ans, only extend reach
            tmpend = max(tmpend, right)
            if tmpend >= T:
                return ans
        return -1

    def videoStitching_wrong(self, clips: List[List[int]], T: int) -> int:
        ans, curend, tmpend = 1, 0, 0
        clips.sort()
        for left, right in clips:
            if left > curend:
                if left > tmpend:
                    return -1
                curend, ans = tmpend, ans + 1

            tmpend = max(tmpend, right)
            if tmpend >= T:
                break
        return ans # only difference but wrong, final return can only be -1 in case all segments visited but cannot reach end.


    # O(max(N, T)), waste time if T >> N due to check all index in a segment
    def videoStitching_ming(self, clips: List[List[int]], T: int) -> int:
        reach = {}
        for s, e, in clips:
            reach[s] = max(e, reach.get(s, s))

        s, e, ans = 0, reach.get(0, 0), 1
        while e > s:
            if e >= T: return ans
            ans += 1
            s, e = e, max(reach.get(i, i) for i in range(s + 1, e + 1)) # check all segment, bad!!
        return -1

print(Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10)) # 3
print(Solution().videoStitching([[0,1],[1,2]], 5)) # -1
print(Solution().videoStitching([
    [0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],
9)) # 3
