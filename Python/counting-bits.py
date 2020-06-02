# Time:  O(n)
# Space: O(n)

# 338
# Given a non negative integer number num. For every numbers i
# in the range 0 <= i <= num calculate the number
# of 1's in their binary representation and return them as an array.
#
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
#
# Follow up:
#
# It is very easy to come up with a solution with run
# time O(n*sizeof(integer)). But can you do it in
# linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using
# any builtin function like __builtin_popcount in c++ or
# in any other language.
# Hint:
#
# 1. You should make use of what you have produced already.
# 2. Divide the numbers in ranges like [2-3], [4-7], [8-15]
#    and so on. And try to generate new range from previous.
# 3. Or does the odd/even status of the number help you in
#    calculating the number of 1s?


class Solution(object):
    # if i odd: res[i-1] + 1; if i even: res[i>>1].
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, num + 1):
            res.append(res[-1] + 1 if i & 1 else  res[i >> 1])
        return res

    # 2^n ... 2^(n+1)-1 have a leading 1 comparing to 0 ... 2^n-1
    def countBits2(self, num):
        s = [0]
        while len(s) <= num:
            s.extend(list(map(lambda x: x + 1, s)))
        return s[:num + 1]


if __name__ == '__main__':
    r = Solution().countBits(17)
    print(r) # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2]
