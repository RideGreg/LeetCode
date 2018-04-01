class Solution(object):
    def monotoneIncreasingDigits(self, N):
        if N < 10:
            return N
        s = str(N)
        length = len(s)
        for i in xrange(len(s) - 1):
            if s[i] > s[i + 1]:
                for j in xrange(i, -1, -1):
                    if j == 0 or s[j] != s[j-1]:
                        pre = s[:j + 1]
                        cnt = length - (j + 1)
                        return int(pre) * pow(10, cnt) -1
        return N

'''
        if N < 10:
            return N
        s = str(N)
        length = len(s)
        for i in xrange(len(s) - 1):
            if s[i] > s[i + 1]:
                pre = ''
                if i == 0:
                    pre = s[0]
                    cnt = length-1
                else:
                    for j in xrange(i, -1, -1):
                        if s[j] != s[i]:
                            pre = s[:j + 2]
                            cnt = length - (j + 2)
                            break
                    if not pre:
                        pre = s[0]
                        cnt = length - 1
                return int(pre) * pow(10, cnt) -1
        return N  
'''
print Solution().monotoneIncreasingDigits(393457075)
print Solution().monotoneIncreasingDigits(1234)
print Solution().monotoneIncreasingDigits(332)
print Solution().monotoneIncreasingDigits(1332)
print Solution().monotoneIncreasingDigits(1232)
print Solution().monotoneIncreasingDigits(1)
print Solution().monotoneIncreasingDigits(603253281)


