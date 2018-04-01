class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param logs: Sequence of processes
    @param queries: Sequence of queries
    @return: Return the number of processes
    """
    def numberOfProcesses(self, logs, queries):
        logs.sort(key=lambda x:(x.start, x.end))
        l = len(logs)
        ans = []
        for q in queries:
            i, j = 0, l-1
            cnt = 0
            while i<=j:
                m = (j-i)/2+i
                if logs[m].start > q:
                    j = m - 1
                else:
                    i = m + 1
            for k in xrange(j+1):
                if logs[k].end >= q:
                    cnt+=1
            ans.append(cnt)
        return ans

print Solution().numberOfProcesses(
[
 Interval(  2255907,  44836419),
 Interval(  8000719,  95236027),
 Interval( 25960936, 731655112),
 Interval( 27303361, 716044243),
 Interval( 75634358, 115570826),
 Interval( 90803241, 265311561),
 Interval(266725056, 567494217),
 Interval(323590401, 608580695),
 Interval(364293775,1052503147),
 Interval(680417571, 740927995)],
[138303481,305539591,138113185,102644275,653265601,241720193,188734546,
 123232425,322162573,528753202,436683931,153333603,686299562])
#print Solution().numberOfProcesses([Interval(2,1234), Interval(1,1234)], [2])
#print Solution().numberOfProcesses([Interval(1,1234), Interval(2,1234)], [1,1235])