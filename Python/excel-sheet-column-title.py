# Time:  O(logn)
# Space: O(1)

# 168
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, dvd = "", n

        while dvd:
            result += chr((dvd - 1) % 26 + ord('A'))
            dvd = (dvd - 1) // 26

        return result[::-1]


if __name__ == "__main__":
    for i in range(1, 27):
        print(Solution().convertToTitle(i)) # 'A B ... Z'
        print(Solution().convertToTitle(26*2+i)) # 'BA BB ... BZ'
        print(Solution().convertToTitle(26**2*4+26+i)) # 'DAA DAB ... DAZ'
