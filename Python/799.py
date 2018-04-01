class Solution(object):
    def champagneTower(self, p, r, g):
        row = [poured*1.0]
        for _ in xrange(query_row):
            newRow = [0.0] * (len(row)+1)
            for i in xrange(len(row)):
                if row[i] > 1:
                    newRow[i] += (row[i]-1)/2.0
                    newRow[i+1] += (row[i]-1)/2.0
            row = newRow
        return min(1.0, row[query_glass])

print Solution().champagneTower(6,2,0)
