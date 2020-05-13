# Time:  O(logn)
# Space: O(1)

# 1009
# Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary,
# 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.
#
# The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.
# For example, the complement of "101" in binary is "010" in binary.
#
# For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

class Solution(object):
    def bitwiseComplement(self, N): # USE THIS: bit op
        """
        :type N: int
        :rtype: int
        """
        if N == 0: return 1
        ans, power = 0, 0
        while N:
            N, d = divmod(N, 2)
            ans += (1 - d) * (2 ** power)
            ''' OR USE BIT OP
            b = (N & 1) ^ 1    # "与"下来
            N >>= 1
            if b:
                ans |= b << power  # "或"上去
            '''
            power += 1
        return ans


    # what is the relationship between input and output
    # input + output = 111....11 in binary format
    # Is there any corner case?
    # 0 is a corner case expecting 1, output > input
    # Let's find mask, which is the first number X that X = 1111....1 >= N
    def bitwiseComplement_mask(self, N):
        mask = 1
        while N > mask:
            mask = mask*2+1  # 0b1, 0b11, 0b111 ...
        return mask-N   # or mask ^ N


    def bitwiseComplement_strConversion(self, N):
        s = bin(N)[2:]
        a = list(s)
        a = map(lambda c: 1-int(c), a)
        a = map(str, a)
        return int(''.join(a), 2)

print(Solution().bitwiseComplement(5)) # 2
print(Solution().bitwiseComplement(7)) # 0
print(Solution().bitwiseComplement(10)) # 5