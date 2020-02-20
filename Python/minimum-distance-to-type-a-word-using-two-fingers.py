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
    # Time:  O(52n)
    # Space: O(52)
    def minimumDistance(self, word): # USE THIS: calculate the total distance by using finger 1 or 2 for each char
        def distance(a, b):
            if -1 in [a, b]:
                return 0
            return abs(a//6 - b//6) + abs(a%6 - b%6)

        dp = {(-1, -1): 0} # {finger1, finger2}
        for c in word:
            c = ord(c)-ord('A')
            ndp = {}
            for a, b in dp:
                ndp[c, b] = min(ndp.get((c, b), float("inf")), dp[a, b] + distance(a, c))
                ndp[a, c] = min(ndp.get((a, c), float("inf")), dp[a, b] + distance(b, c))
            dp = ndp
        return min(dp.values())

    def minimumDistance2(self, word):
        """
        :type word: str
        :rtype: int
        """
        def distance(a, b):
            return abs(a//6 - b//6) + abs(a%6 - b%6)
        # dp[i] stores the cost of char i to its next char in string. max(dp) is where to change finger after that char.
        # All previous savings from changing hands are accumulated.
        dp = [0]*26
        for i in range(len(word)-1):
            b, c = ord(word[i])-ord('A'), ord(word[i+1])-ord('A')
            # the selected 'a' should just before 'c' for optimal path. If a same as c, means c is beginning of 2nd finger.
            dp[b] = max(dp[a] - distance(a, c) + distance(b, c) for a in range(26))
        seq = sum(distance(ord(word[i])-ord('A'), ord(word[i+1])-ord('A')) for i in range(len(word)-1))
        return seq - max(dp)


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
# algorithm2: 2+5+1-max(dp {'A':5, 'C':2, 'K':1})
print(Solution().minimumDistance("HAPPY")) # 6: 0 (f1 on H) + 2 (f1 on A) + 0 (f2 on P) + 0 (f2 on P) + 4 (f1 on Y)
# algorithm2: 2+5+0+5-max(dp {'A':5, 'H':2, 'P':6})
print(Solution().minimumDistance("NEW")) # 3. algorithm2: 5+3-max(dp={'E':4, 'N':5})
print(Solution().minimumDistance("YEAR")) # 7. algorithm2: 8+4+7-max(dp={'A':12, 'E':8, 'Y':8})