import collections
class Solution(object):
    def canTransform(self, start, end):
        if len(start) != len(end):
            return False
        if start == end: return True
        used = {}
        q = collections.deque([start])
        while q:
            cur = q.popleft()
            used[cur] = 1
            for i in xrange(len(cur)-1):
                if cur[i:i+2] == 'XL':
                    nxt = cur[:i] + 'LX' + cur[i+2:]
                    if nxt == end:
                        return True
                    if nxt not in used:
                        q.append(nxt)
                elif cur[i:i+2] == 'RX':
                    nxt = cur[:i] + 'XR' + cur[i+2:]
                    if nxt == end:
                        return True
                    if nxt not in used:
                        q.append(nxt)
        return False

#print Solution().canTransform("RXXLRXRXL", "XRLXXRRLX")
print Solution().canTransform("XRXXLXLXXXXRXXXXLXXL", "XXRXLXXLXXRLXXXLXXXX")
