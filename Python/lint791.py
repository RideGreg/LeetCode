class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """
    def mergeNumber(self, numbers):
        def helper(num):
            if len(num) == 2:
                return sum(num)
            s = num[-1]+num[-2]
            del num[-2:]
            inserted = False
            for i in reversed(xrange(len(num))):
                if s <= num[i]:
                    num.insert(i+1, s)
                    inserted = True
                    break
            if not inserted: num.insert(0, s)
            return helper(num) + s
        return helper(sorted(numbers, reverse=True))

        '''
        def helper(num):
            if len(num) == 2:
                return sum(num)
            m1, m2 = float('inf'), float('inf')
            i1, i2 = 0, 0
            for i, x in enumerate(num):
                if x <= m1:
                    m1, m2, i1, i2 = x, m1, i, i1
                elif x < m2:
                    m2, i2 = x, i
            s = num[i1]+num[i2]
            i1, i2 = max(i1, i2), min(i1, i2)
            del num[i1]
            del num[i2]
            num.append(s)
            return helper(num) + s
        return helper(numbers)
        '''

print Solution().mergeNumber([1,2,3,4])
print Solution().mergeNumber([4,2,3,1])
print Solution().mergeNumber([4,2,8,1])
