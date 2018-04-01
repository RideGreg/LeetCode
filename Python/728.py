class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans = []
        for i in xrange(left, right+1):
            s = str(i)
            if all(c is not '0' and i % int(c) == 0 for c in s):
#            valid = 1
#            for c in s:
#                if c is '0' or i % int(c) != 0:
#                    valid = 0
#                    break
#            if valid:
                ans.append(i)
        return ans

print Solution().selfDividingNumbers(1,22)