# Time:  O(m * n)
# Space: O(m + n)

# 43
# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note: The numbers can be arbitrarily large and are non-negative.
#

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0]*(len(num1)+len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                result[i+j+1] += int(num1[i])*int(num2[j])
                result[i+j] += result[i+j+1]//10
                result[i+j+1] %= 10
        for i in range(len(result)):
            if result[i]:
                return "".join(map(lambda x: str(x), result[i:]))
        return "0"

# Time:  O(m * n)
# Space: O(m + n)
class Solution2(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        # Skip leading 0s.
        i = len(res) - 1
        while i > 0 and res[i] == 0:
            i -= 1

        return "".join(map(str, result[i::-1]))

# Time:  O(m * n)
# Space: O(m + n)
# Using built-in bignum solution.
class Solution3(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    print Solution().multiply("123", "1000")
