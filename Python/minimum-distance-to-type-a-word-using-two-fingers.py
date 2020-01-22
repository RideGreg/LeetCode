# Time:  O(26n)
# Space: O(26)

# 1320 weekly contest 171 1/11/2020

# A B C D E F
# G H I J K L
# M N O P Q R
# S T U V W X
# Y Z

# You have a keyboard layout as shown above in the XY plane, where each English uppercase letter is located at some coordinate,
# for example, the letter A is located at coordinate (0,0), the letter B is located at coordinate (0,1), the letter P is
# located at coordinate (2,3) and the letter Z is located at coordinate (4,1).
#
# Given the string word, return the minimum total distance to type such string using only two fingers. The distance
# between coordinates (x1,y1) and (x2,y2) is |x1 - x2| + |y1 - y2|.
#
# Note that the initial positions of your two fingers are considered free so don't count towards your total distance,
# also your two fingers do not have to start at the first letter or the first two letters.

class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def distance(a, b):
            return abs(a//6 - b//6) + abs(a%6 - b%6)

        dp = [0]*26
        for i in range(len(word)-1):
            b, c = ord(word[i])-ord('A'), ord(word[i+1])-ord('A')
            dp[b] = max(dp[a] - distance(a, c) + distance(b, c) for a in range(26))
        return sum(distance(ord(word[i])-ord('A'), ord(word[i+1])-ord('A')) for i in range(len(word)-1)) - max(dp)


# Time:  O(52n)
# Space: O(52)
class Solution2(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def distance(a, b):
            if -1 in [a, b]:
                return 0
            return abs(a//6 - b//6) + abs(a%6 - b%6)

        dp = {(-1, -1): 0}
        for c in word:
            c = ord(c)-ord('A')
            new_dp = {}
            for a, b in dp:
                new_dp[c, b] = min(new_dp.get((c, b), float("inf")), dp[a, b] + distance(a, c))
                new_dp[a, c] = min(new_dp.get((a, c), float("inf")), dp[a, b] + distance(b, c))
            dp = new_dp
        return min(dp.itervalues())

    # This solution is wrong. This is one hand, then another hand.
    def minimumDistance_wrong(self, word: str) -> int:
        ans = []
        c1 = word[0]
        x1, y1 = divmod(ord(c1)-ord('A'), 6)
        x2, y2 = None, None
        for c2 in word[1:]:
            x2, y2 = divmod(ord(c2)-ord('A'), 6)
            ans.append(abs(x1-x2)+abs(y1-y2))
            x1, y1 = x2, y2
        return sum(ans)-max(ans)

print(Solution().minimumDistance("CAKE")) # 3: 0 (f1 on C) + 2 (f1 on A) + 0 (f2 on K) + 1 (f2 on E)
print(Solution().minimumDistance("HAPPY")) # 6: 0 (f1 on H) + 2 (f1 on A) + 0 (f2 on P) + 0 (f2 on P) + 4 (f1 on Y)
print(Solution().minimumDistance("NEW")) # 3
print(Solution().minimumDistance("YEAR")) # 7