# Time:  O(n)
# Space: O(1)

# 1247 weekly contest 161 11/2/2019

# You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only.
# Your task is to make these two strings equal to each other. You can swap any two characters
# that belong to different strings, which means: swap s1[i] and s2[j].
#
# Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

class Solution(object):
    def minimumSwap(self, s1, s2): # USE THIS
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        x1, y1 = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x': x1 += 1
                else: y1 += 1
        if (x1+y1) % 2:  # impossible
            return -1
        # case1: per xx or yy needs one swap, (x1//2 + y1//2) 
        # case2: per xy or yx needs two swaps, (x1%2 + y1%2)
        return (x1//2 + y1//2) + (x1%2 + y1%2)


    def minimumSwap_ming(self, s1: str, s2: str) -> int:
        n = len(s1)
        xcnt, ycnt, ans = 0, 0, 0
        for i in range(n):
            if s1[i] == 'x' and s2[i] == 'y':
                if xcnt > 0: # got 'xx' vs 'yy'
                    xcnt -= 1
                    ans += 1
                else:
                    xcnt += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                if ycnt > 0: # got 'yy' vs 'xx'
                    ycnt -= 1
                    ans += 1
                else:
                    ycnt += 1

        if xcnt == ycnt: # 'xy' vs 'yx'
            return ans + xcnt * 2
        else:
            return -1

print(Solution().minimumSwap('xx', 'yy')) # 1
print(Solution().minimumSwap('xy', 'yx')) # 2
print(Solution().minimumSwap('xx', 'xy')) # -1
print(Solution().minimumSwap('xxyyxyxyxx', 'xyyxyxxxyx')) # 4