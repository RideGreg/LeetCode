# Time:  O(n)
# Space: O(n)

# 1003
# We are given that the string "abc" is valid.
#
# From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y)
# is equal to V.  (X or Y may be empty.)  Then, X + "abc" + Y is also valid.
#
# If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc".
# Examples of invalid strings are: "abccba", "ab", "cababc", "bac".
#
# Return true if and only if the given string S is valid.

class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for i in S:
            if i == 'c':
                if stack[-2:] == ['a', 'b']:
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack


    # Time is not good, scan S multiple times
    def isValid2(self, S):
        while 'abc' in S:
            S = S.replace('abc', '')
        return not S


    # TLE: Time O(n^2) Every time you replace "abc", you are creating a new string.
    # You may creat n possible string. For each string, you do a find and replace which is O(n).
    def isValid_TLE(self, S):  # TLE: if abc at the end of S, repeat scan most front part of S without vain
        if len(S) % 3: return False
        if S == 'abc': return True
        for i in range(len(S)-2):
            if S[i:i+3] == 'abc':
                return self.isValid(S[:i]+S[i+3:])
        return False


print(Solution().isValid("abcabcababcc")) # True
print(Solution().isValid("abccba")) # True
