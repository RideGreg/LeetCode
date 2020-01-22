# Time:  O(31)
# Space: O(1)

# 1318 weekly contest 171 1/11/2020

# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make a OR b == c. (bitwise OR operation).

# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

# Example: Input a = 2 (0010), b = 6 (0110), c = 5 (0101). Output 3
# 0010       0001
# 0110       0100
# ----- =>  ------
# 0101       0101

class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def number_of_1_bits(n):
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        return number_of_1_bits((a|b)^c) + number_of_1_bits(a&b&~c)


# Time:  O(31)
# Space: O(1)
class Solution2(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        result = 0
        for i in xrange(31):
            a_i, b_i, c_i = map(lambda x: x&1, [a, b, c])
            if (a_i | b_i) != c_i:
                result += 2 if a_i == b_i == 1 else 1
            a, b, c = a >> 1, b >> 1, c >> 1
        return result

    def minFlips_ming(self, a: int, b: int, c: int) -> int:
        a = bin(a)[:1:-1]
        b = bin(b)[:1:-1]
        c = bin(c)[:1:-1]
        l = max(len(a), len(b), len(c))
        ans = 0
        for i in range(l):
            av = int(a[i]) if i < len(a) else 0
            bv = int(b[i]) if i < len(b) else 0
            cv = int(c[i]) if i < len(c) else 0
            if cv and av == 0 and bv == 0:
                ans += 1
            elif cv == 0:
                ans += int(av!=0)+int(bv!=0)
        return ans

print(Solution().minFlips(2,6,5)) # 3
print(Solution().minFlips(4,2,7)) # 1
print(Solution().minFlips(1,2,3)) # 0
