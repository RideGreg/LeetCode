class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        '''
        if sx == tx and sy == ty:
            return True
        import collections
        used = {}
        used[(sx,sy)] = True
        q = collections.deque([(sx,sy)])
        while q:
            x, y = q.popleft()
            for curx, cury in [(x, x+y), (x+y, y)]:
                if curx == tx and cury == ty:
                    return True
                if curx <= tx and cury <= ty and (curx, cury) not in used:
                    used[(curx, cury)] = True
                    q.append((curx, cury))
        return False
        '''
        if sx == tx and sy == ty: return True
        if sx > tx or sy > ty: return False
        m = [[0]* (ty+1) for _ in xrange(tx+1)]
        m[sx][sy]=1
        for i in xrange(sx,len(m)):
            for j in xrange(sy,len(m[0])):
                if (0<=i-j<len(m) and m[i-j][j]==1) or (0<=j-i<len(m[0]) and m[i][j-i]==1):
                    m[i][j]=1
        return m[-1][-1] == 1

print Solution().reachingPoints(1,1,3,5)
print Solution().reachingPoints(1,1,2,2)
print Solution().reachingPoints(1,1,1,1)
