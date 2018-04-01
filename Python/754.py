import math
class Solution(object):
    def reachNumber(self, target):
        def is_sq(a):
            root = math.sqrt(a)
            return int(root+0.5)**2 == a
        target = abs(target)
        while 1:
            if is_sq(1+8*target):
                return int(math.sqrt(1+8*target) - 1) / 2
            target += 2
        '''
        old, new, ans = set([0]), set(), 0
        if target == 0: return ans
        while 1:
            ans += 1
            for n in old:
                #print n
                a, b = n+ans, n-ans
                if target == a or target == b:
                    return ans
                new.add(a)
                new.add(b)
            old, new = new, set()'''

print Solution().reachNumber(3)
print Solution().reachNumber(2)
print Solution().reachNumber(0)


