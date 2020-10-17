from typing import List

# 1. 给你一个n * n 的矩阵， 分成size * size的block
# 按照每一个小block的first missing positive 按照从左到右 从上到下的方式rearrange 这个矩阵
# def rearrangeMatrix(self, grid, sz):

# 2. 给你一个 字符串 和一个 数字n， 问你字符串能不能被分割成n 个Palindrome，可以乱序，比较容易

# 3. 一个function是给一个string A，和另外一个list of string L，输出是判断 A 是不是由0 到 i的string
# 按照index的顺序组成的。注意，L.0 + L.1 + ... + L.i 不是 随便什么顺序。
# 最后，再给list of A，判断哪几个A是由L里面的string组合的
# def foo(A, L):
#   lA, start = len(A), 0
#   for i, s in enumerate(L)):
#     .. start+len(s) <= lA
#     .. A[start:start+len(s)] == s
#     .. start += len(s)

# 4. 一个text editor，应该是常见的那个题目。不难，就是繁琐，有什么COPY，INSERT，DELETE functions，
# 然后，还有UNDO，clipboard。然后给一串输入，看你输出是否正确。测试只对了一半，我后面发现UNDO是不能用于COPY的，
# 可能是这个地方错了。

# 5. sort parallel diagonal string

# 6. 有一个integer array， 要将array分成三个subarray要求1st subarray小于等于 2nd subarray sum，
# 2nd subarray sum 小于等于 3rd subarray sum。 return所有可能的partition的个数
# [1, 1, 2, 1, 2, 3, 1]
#psum [1,2,4,5,7,10,11] O(nlogn) xxxxixxxjxxxx iterate i, then binary search to find range of j

# 7. numberSigningSum: given an integer, return the sum of its digits (alternating positive and negative)
# e.g 14258 => 1 - 4 + 2 - 5 + 8 = 2, 142586 => 1 - 4 + 2 - 5 + 8 - 6 = -4

# 8. concatSwaps: given a string 's', an integer array 'A', sum of A equals to the length of s.
# Get the substrings whose lengths equal to intergers in A, swap substrings in pair (if last integer
# is signle, no need to swap it), return concatenation of substrings.
# E.g. 'codesignal' [3,2,1,3,1] => 'escodgnail'
# E.g. 'codesignal' [3,2,1,4]   => 'escodgnali'

# 9. constructorNames: given 2 strings s1 and s2, return whether one can convert to the other. The rule
# of conversion is:
# either swap 2 characters in a string; or
# swap all appearance of 2 charactors (e.g. all 'c' become 'z' and all 'z' become 'c')
# e.g. 'babcccz' can convert to 'abbczzz' (babcccz -> abbcccz -> abbzzzc -> abbczzz)
# e.g. 'bad' can NOT convert to 'aba'

# 10. maxArithmeticLength: given 2 integer arrays A and B, each are sorted ascending, each contains
# NO DUPLICATE integers. The length of A or B is between 2 and 1000. You can
# take any integer from B and insert to A at any position. The goal is to make A as an arithmetic
# sequence, return the length of longest possible arithmetic sequence. Return -1 if impossible
# to make A as an arithmetic sequence.
# e.g. A = [4, 8, 16], B = [-4, 0, 2, 6, 12, 20, 22, 28] => 7 (the sequence is [-4,0,4,8,12,16,20])
# e.g. A = [3, 5, 8], B = [2, 6, 9] => -1

import collections, math

class Solution(object):
    # 1. 给你一个n * n 的矩阵， 分成size * size的block
    # 按照每一个小block的first missing positive 按照从左到右 从上到下的方式rearrange 这个矩阵
    def rearrangeMatrix(self, grid, sz):
        def findMissing(inset):
            ans = 1
            while ans in inset:
                ans += 1
            return ans


        n = len(grid)
        cnt = n // sz
        #coord2missing = {} # put in a dict, and sort
        ordered = [] # put in a list of tuple, and sort
        for k in range(cnt*cnt):
            xid, yid = divmod(k, cnt)
            x0, y0 = xid * sz, yid * sz
            seen = {grid[x0+dx][y0+dy] for dx in range(sz)
                    for dy in range(sz)}
            '''
            seen = set()
            for dx in range(sz):
                for dy in range(sz):
                    seen.add(grid[x0+dx][y0+dy])'''
            ordered.append([findMissing(seen), (x0, y0)])
            # missing num can be duplicate, so cannot be key
            #coord2missing[(x0, y0)] = findMissing(seen)

        #ordered = sorted(coord2missing, key=coord2missing.get)
        ordered = [x[1] for x in sorted(ordered)]
        ans =[list(row) for row in grid]
        for k in range(cnt*cnt):
            xid, yid = divmod(k, cnt)
            x0, y0 = xid * sz, yid * sz
            srcx0, srcy0 = ordered[k]
            if (x0, y0) != (srcx0, srcy0):
                for dx in range(sz):
                    ans[x0+dx][y0 : y0 + sz] = grid[srcx0+dx][srcy0 : srcy0 + sz]
        return ans

    # 2. 给你一个 字符串 和一个 数字n， 问你字符串能不能被分割成n 个Palindrome，可以乱序，比较容易

    # 5. sort parallel diagonal string
    #def sortDiagonal(self, grid):
    #    ordered, n = [], len(grid)

    # 7. numberSigningSum: given an integer, return the sum of its digits (alternating positive and negative)
    def numberSigningSum(self, n):
        ans = 0
        digitCnt = len(str(n))
        sign = 1 if digitCnt % 2 == 1 else -1
        while n:
            n, v = divmod(n, 10)
            ans += v * sign
            sign *= -1
        return ans

    def concatSwaps(self, s, sizes): # 8
        ll = len(sizes)
        ans, start = [''] * ll, 0
        for i, sz in enumerate(sizes):
            # find swapped index
            i = i+1 if i % 2 == 0 else i-1
            if i >= ll: # revert last single index
                i -= 1
            ans[i] = s[start : start + sz]
            start += sz
        return ''.join(ans)

    def constructorNames(self, src, dest): # 9
        s, d = collections.Counter(src), collections.Counter(dest)
        return set(s.keys()) == set(d.keys()) and sorted(s.values()) == sorted(d.values())

    def maxArithmeticLength(self, A, B):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def getFactors(n):
            ans = {1, n}
            factor = 2
            while factor <= int(math.sqrt(n)):
                if n % factor == 0:
                    ans.add(factor)
                    ans.add(n // factor)
                factor += 1
            return sorted(ans)

        cand, minA, maxA = set(A+B), min(A), max(A)
        diff = [A[i+1] - A[i] for i in range(len(A)-1)]
        # input array A and B each doesn't contain duplicate, so doesn't need to consider minDiff = 0
        minDiff = diff[0]
        for x in diff[1:]:
            minDiff = gcd(minDiff, x)

        ans = -1
        for d in getFactors(minDiff):
            for x in range(minA, maxA+1, d):
                if x not in cand:
                    break
            else:
                # extend to both sides
                mn = minA
                while mn - d in cand:
                    mn = mn - d
                mx = maxA
                while mx + d in cand:
                    mx = mx + d
                ans = max(ans, (mx - mn) // d + 1)
        return ans

'''
print(Solution().rearrangeMatrix([
    [1,2,3,4],
    [5,6,7,8],
    [3,2,1,4],
    [1,5,2,3]
], 2)) # [[3, 4, 1, 2], [7, 8, 5, 6], [3, 2, 1, 4], [1, 5, 2, 3]]
# missing: [[3,1], [4,5]]

print(Solution().rearrangeMatrix([
    [1,2,3,4],
    [5,6,7,8],
    [3,8,1,4],
    [1,5,5,3]
], 2)) # [[3, 4, 3, 8], [7, 8, 1, 5], [1, 4, 1, 2], [5, 3, 5, 6]]
# missing: [[3,1], [2,2]]

print(Solution().rearrangeMatrix([
    [1,2,3,4,9,1],
    [5,6,7,8,3,2],
    [3,2,1,4,8,1],
    [1,5,2,3,7,6],
    [2,1,9,7,3,1],
    [0,6,8,8,1,3]
], 2)) # missing: [[3,1,4], [4,5,2], [3,1,2]], ans: [
# [3, 4, 9, 7, 8, 1],
# [7, 8, 8, 8, 7, 6],
# [3, 1, 1, 2, 2, 1],
# [1, 3, 5, 6, 0, 6],
# [9, 1, 3, 2, 1, 4],
# [3, 2, 1, 5, 2, 3]]
'''
print(Solution().numberSigningSum(14258)) # 2
print(Solution().numberSigningSum(142586)) # -4

print(Solution().concatSwaps('codesignal', [3,2,1,3,1])) # 'escodgnail'
print(Solution().concatSwaps('codesignal', [3,2,2,3]))   # 'escodnalig'

print(Solution().constructorNames('babcccz', 'abbczzz')) # True
print(Solution().constructorNames('bad', 'aba')) # False

print(Solution().maxArithmeticLength([4, 8, 16], [-4, 0, 2, 6, 12, 20, 22, 28])) # 7
print(Solution().maxArithmeticLength([3, 5, 8], [2, 6, 9])) # -1