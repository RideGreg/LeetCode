import collections
class Solution(object):
    def openLock(self, deadends, target):
        dead = set(deadends)
        used = set()
        ans = -1
        if '0000' in dead:
            return -1
        if target == '0000':
            return 0

        queue = collections.deque([])
        queue.append(('0000', 0))
        while queue:
            cur, turns = queue.popleft()
            used.add(cur)
            for i in xrange(4):
                if cur[i] == '0':
                    next1 = cur[:i]+'9'+cur[i+1:]
                    next2 = cur[:i]+'1'+cur[i+1:]
                elif cur[i] == '9':
                    next1 = cur[:i]+'8'+cur[i+1:]
                    next2 = cur[:i]+'0'+cur[i+1:]
                else:
                    next1 = cur[:i]+str(int(cur[i])-1)+cur[i+1:]
                    next2 = cur[:i]+str(int(cur[i])+1)+cur[i+1:]
#                print "next1, next2 is", next1, next2
                for nxt in [next1, next2]:
                    if nxt not in dead and nxt not in used:
                        if nxt == target:
                            return turns+1
                        queue.append((nxt, turns+1))
                        used.add(nxt)
#                        print queue
        return ans

#print Solution().openLock(['0000'], '8888') #-1
#print Solution().openLock(['0001'], '1000') #1
#print Solution().openLock(['0001'], '0011') #2
#print Solution().openLock(['0001', '0010'], '0011') #4
#print Solution().openLock(["0201","0101","0102","1212","2002"], '0202') #6
#print Solution().openLock(['8888'], '0009') #1
print Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888') #-1
