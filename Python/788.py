class Solution(object):
    def rotatedDigits(self, N):
        ans = 0

        for num in xrange(N+1):
            flag = False
            n = num%10
            if n in [3,4,7]:continue
            if n in [2,5,6,9]: flag = True
            if num>9:
                n = num/10%10
                if n in [3, 4, 7]: continue
                if n in [2, 5, 6, 9]: flag = True
            if num > 99:
                n = num / 100 % 10
                if n in [3, 4, 7]: continue
                if n in [2, 5, 6, 9]: flag = True
            if num > 900:
                n = num / 1000 % 10
                if n in [3, 4, 7]: continue
                if n in [2, 5, 6, 9]: flag = True
            if flag:
                ans+=1
        return ans
        '''
        #ones
        ans = 0
        n, m = N/10, N%10
        ans += 4*n
        if 2<=m: ans += 1
        if 5<=m: ans += 1
        if 6<=m: ans += 1
        if 9<=m: ans += 1
        #tens
        n, m = N/100, N%100
        ans += 24*n
        nums=[20,21,23,24,27,28,
              50,51,53,54,57,58,
              60,61,63,64,67,68,
              90,91,93,94,97,98]
        for num in nums:
            if num<=m: ans += 1
        #hun
        n, m = N/1000, N%1000
        ans += 4*n*(100-40-24)
        if n in [2,5,6,9]:
            for num in xrange(n*1000, N+1):
                if num%10 not in [2,5,6,9] and \
                    num/10%10 not in [2, 5, 6, 9] and \
                    num / 100 % 10 not in [2, 5, 6, 9]:
                    ans+=1
        return ans
        '''

print Solution().rotatedDigits(10)
print Solution().rotatedDigits(857)
#print Solution().rotatedDigits(150)
#print Solution().rotatedDigits(1030)
