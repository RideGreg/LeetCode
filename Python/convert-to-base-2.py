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
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        res = []
        while N:
            res.append(-N & 1)  # N % -2
            N = -(N >> 1)  # N //= -2

        return "".join(map(str, res[::-1])) if res else "0"

    def base2(self, x):
        res = []
        while x:
            res.append(x & 1)
            x = x >> 1
        return "".join(map(str, res[::-1] or [0]))

    def baseNeg2_recur(self, N):
        if N == 0 or N == 1: return str(N)
        return self.baseNeg2(-(N >> 1)) + str(N & 1)


# Time:  O(logn)
# Space: O(1)
class Solution2(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        BASE = -2
        result = []
        while N:
            N, r = divmod(N, BASE)
            if r < 0:
                r -= BASE
                N += 1
            result.append(str(r))
        result.reverse()
        return "".join(result) if result else "0"

print(Solution().baseNeg2(6)) # '11010' (16, -8, 0, -2, 0)
print(Solution().baseNeg2(3)) # '111' (4, -2, 1)