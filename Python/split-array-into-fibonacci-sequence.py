# Time:  O(n^3)
# Space: O(n)

# 842
# Given a string S of digits, such as S = "123456579",
# we can split it into a Fibonacci-like sequence [123, 456, 579].
#
# Formally, a Fibonacci-like sequence is a list F of non-negative
# integers such that:
#
# 0 <= F[i] <= 2^31 - 1,
# (that is, each integer fits a 32-bit signed integer type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# Also, note that when splitting the string into pieces,
# each piece must not have extra leading zeroes,
# except if the piece is the number 0 itself.
#
# Return any Fibonacci-like sequence split from S,
# or return [] if it cannot be done.
#
# Example 1:
#
# Input: "123456579"
# Output: [123,456,579]
# Example 2:
#
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
# Example 3:
#
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
# Example 4:
#
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
# Example 5:
#
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
#
# Note:
# - 1 <= S.length <= 200
# - S contains only digits.


# Solution: Brute Force
# The first two elements of the array uniquely determine the rest of the sequence.
# For each of the first two elements, assuming they have no leading zero, let's iterate through the rest of the string.
# At each stage, we expect a number less than or equal to 2^31 - 1 that starts with the sum of the two previous numbers.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def splitIntoFibonacci(self, S): # 20ms
        """
        :type S: str
        :rtype: List[int]
        """
        for i in xrange(min(10, len(S)-2)):
            a = S[:i+1]
            if a.startswith('0') and a != '0': break
            a = int(a)
            for j in xrange(i+1, min(i+10, len(S)-1)):
                b = S[i+1:j+1]
                if b.startswith('0') and b != '0': break
                b = int(b)
                fib = [a, b]
                k = j+1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31-1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []

    def splitIntoFibonacci_kamyu(self, S):
        def startswith(S, k, x):
            y = 0
            for i in xrange(k, len(S)):
                y = 10*y + int(S[i])
                if y == x:
                    return i-k+1
                elif y > x:
                    break
            return 0

        MAX_INT = 2**31-1
        a = 0
        for i in xrange(len(S)-2):
            a = 10*a + int(S[i])
            b = 0
            for j in xrange(i+1, len(S)-1):
                b = 10*b + int(S[j])
                fib = [a, b]
                k = j+1
                while k < len(S):
                    if fib[-2] > MAX_INT-fib[-1]:
                        break
                    c = fib[-2]+fib[-1]
                    length = startswith(S, k, c)
                    if length == 0:
                        break
                    fib.append(c)
                    k += length
                else:
                    return fib
                if b == 0:
                    break
            if a == 0:
                break
        return []

    # Bad time complexity 240 ms, try to determine first 3 numbers in fib sequence at once.
    # repeat partition with same first number ...
    # not good as the official solution which calculates each first number only once
    def splitIntoFibonacci_mingContest(self, S):
        def isF(ss):
            for i in xrange(1, min(11, len(ss)-1)):
                for j in xrange(i+1, len(ss)):
                    d1, d2, d3 = ss[:i], ss[i:j], ss[j:]
                    fail = False
                    for d in (d1,d2,d3):
                        if len(d)>1 and d[0]=='0' or int(d)>2147483647:
                            fail = True
                            break
                    if fail: continue
                    if int(d1)+int(d2)==int(d3):
                        #print '{} {} {}'.format(d1, d2, d3)
                        return [int(d1),int(d2),int(d3)]
            return []

        if len(S)<3: return False
        ans = []
        for i in xrange(3, min(31, len(S)+1)):
            ans = []
            ret = isF(S[:i])
            if ret:
                ans = ret
                d2, d3 = ret[1], ret[2]
                ok = True
                while i < len(S) and ok:
                    if d2+d3 > 2147483647:
                        ok = False
                        break
                    nd = str(d2 + d3)
                    if i + len(nd) <= len(S) and nd == S[i:i+len(nd)]:
                        i += len(nd)
                        d2, d3 = d3, d2+d3
                        ans.append(d3)
                    else:
                        ok = False
                if i==len(S) and ok: return ans
        return ans

print Solution().splitIntoFibonacci('123456579') # [123, 456, 579]
print Solution().splitIntoFibonacci('11235813') # [1, 1, 2, 3, 5, 8, 13]
print Solution().splitIntoFibonacci('112358130') # []
print Solution().splitIntoFibonacci('0123') # []
print Solution().splitIntoFibonacci('1101111') # [11, 0, 11, 11]