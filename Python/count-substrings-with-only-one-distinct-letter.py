# Time:  O(n)
# Space: O(1)

# 1180
# Given a string S, return the number of substrings that have only one distinct letter.

# 1 <= S.length <= 1000
# S[i] consists of only lowercase English letters.
# Hint:
# 1. What if we divide the string into substrings containing only one distinct character with maximal lengths?
# 2. Now that you have sub-strings with only one distinct character, Try to come up with a formula that counts the number of its sub-strings.
# 3. Alternatively, Observe that the constraints are small so you can use brute force.

class Solution(object):
    def countLetters(self, S): # USE THIS: two pointers
        """
        :type S: str
        :rtype: int
        """
        result = 0
        left = 0
        for right in range(len(S)):
            if S[right] != S[left]:
                left = right
            result += right-left+1
        return result

    def countLetters2(self, S): # similar to solution 1
        result = len(S)
        left = 0
        for right in range(1, len(S)):
            if S[right] == S[left]:
                result += right-left
            else:
                left = right
        return result

    def countLetters3(self, S): # get width of each block
        left, ans = 0, 0
        for right in range(len(S)+1):
            if right == len(S) or S[right] != S[left]:
                width = right - left
                ans += width * (width+1) // 2
                left = right
        return ans

print(Solution().countLetters("aaaba")) # 8
print(Solution().countLetters("aaaaaaaaaa")) # 55