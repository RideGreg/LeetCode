# Time : O(logn) = O(32)
# Space: O(1)
# 190
# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as
# 00000010100101000001111010011100), return 964176192 (represented in binary
# as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result <<= 1    # this cannot be in end of loop, 不能取值然后移位
            result |= n & 1 # 注意如果写一行 ans << 1 + (n & 1)不对，<<优先级低，应该(ans << 1) + (n & 1)
            n >>= 1
        return result

    def reverseBits2(self, n):
        string = bin(n)
        if '-' in string:
            string = string[:3] + string[3:].zfill(32)[::-1]
        else:
            string = string[:2] + string[2:].zfill(32)[::-1]
        return int(string, 2)

if __name__ == '__main__':
  print(Solution().reverseBits(1)) # 2147483648 '1000 0000 0000 0000 0000 0000 0000 0000'
  print(Solution().reverseBits(12)) # 805306368 '0011 0000 0000 0000 0000 0000 0000 0000'
