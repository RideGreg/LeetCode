# Time:  O(logn)
# Space: O(1)

# 1017
# Given a number N, return a string consisting of "0"s and "1"s that represents its value
# in base -2 (negative two).
#
# The returned string must have no leading zeroes, unless the string is "0".

# Solution: write base2 function first (check last digit, shift to right), then add a - sign.
# Note string concatenation is costly. Instead of create a new string each time,
# we can improve this process using some operations join/reverse or data structure list.

# Theoretically, we are doing N // (-2), but cannot directly use divmod or //, need post-processing.
# divmod(-3, -2) => (1, -1); (-3)//(-2) => 1; (-3)%(-2) => -1
# -((-3)>>1) => -2, as 111101 => 111110  this is correct
# -3&1 => 1, -(-3)&1 => 1

# divmod(3, 2) => (1,1)  divmod(-3, 2) => (-2, 1)  remainder is always 1 (between [0,2])
# divmod(3, -2) => (-2,-1)  divmod(-3, -2) => (1, -1)  remainder is always -1 (between [-2,0])

class Solution(object):
    # 先看2进制的做法
    def base2(self, x):
        if x == 0: return '0'
        res = []
        while x:
            x, r = divmod(x, 2)
            res.append(str(r))
        return "".join(res[::-1])

    # -2进制：除数为-2时，余数只能为0或-1。进制表示中只能使用0或1，所以需要调整余数和商。
    def baseNeg2(self, N: int) -> str: # USE THIS: clearer logic
        if N == 0: return '0'
        result = []
        while N:
            N, r = divmod(N, -2)  # r can be 0 or -1
            if r < 0:
                r -= -2  # 余数置正 -1 -> 1, 并且调整商值
                N += 1
            result.append(str(r))
        result.reverse()
        return "".join(result)

    # replace N%-2 by N%2, replace N//-2 by N//2.
    def baseNeg2_another(self, N):
        res = []
        while N:
            res.append((-N) & 1) # N%-2 = (-N) % 2. Note N%2 and (-N)%2 the result (last digit) is the same
            N = -(N >> 1) # N//-2 = - (N//2) = -1, if N=3. Note (-N) >> 1 is wrong, which is -2 when N=3.

        return "".join(map(str, res[::-1])) if res else "0"

    def baseNeg2_recur(self, N):
        if N == 0 or N == 1: return str(N)
        return self.baseNeg2_recur(-(N >> 1)) + str(N & 1)


print(Solution().baseNeg2(6)) # '11010' (16, -8, 0, -2, 0)
print(Solution().baseNeg2(3)) # '111' (4, -2, 1)