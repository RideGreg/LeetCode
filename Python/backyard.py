class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        if x % 7 == 0:
            return True
        while x > 0:
            if x % 3 == 0:
                return True
            x -= 7
        return False

print Solution().isBuild(10)
print Solution().isBuild(5)

