# Time:  O(n)
# Space: O(h), h is the depth of the recursion

# 394
# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is
# being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
#
# You may assume that the input string is always valid;
# No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not
# contain any digits and that digits are only for those repeat numbers, k.
# For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution(object):
    def decodeString(self, s): # USE THIS
        stack, curNum, curString = [], 0, ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString, curNum = '', 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

    def decodeString_stack2(self, s):
        stack = [["", 1]] # [subs, repeatNum]
        num = 0
        for ch in s:
            if ch.isdigit():
              num = num * 10 + ord(ch) - ord("0")
            elif ch == '[':
                stack.append(["", num])
                num = 0
            elif ch == ']':
                subs, k = stack.pop()
                stack[-1][0] += subs * k
            else:
                stack[-1][0] += ch
        return stack[0][0]

    def decodeString_recur(self, s): # recursion: although some repeat scan, still O(n)
        """
        :type s: str
        :rtype: str
        """
        ans, i, j = '', 0, len(s)
        while i < j:
            if s[i].isalpha():
                ans += s[i]
                i += 1
            elif s[i].isdigit():
                n = 0
                while s[i].isdigit():
                    n = 10 * n + int(s[i])
                    i += 1
                brkt2 = i
                score = 1
                while score != 0: # repeat scan, the substring will be scanned again in recursion
                    brkt2 += 1
                    if s[brkt2] == '[':
                        score += 1
                    elif s[brkt2] == ']':
                        score -= 1
                ans += self.decodeString(s[i + 1:brkt2]) * n
                i = brkt2 + 1

        return ans

    def decodeString_recur2(self, s): # quite some KENG (condition check)
        def foo(s, i):
            ans = ''
            while i < len(s) and s[i] != ']':
                if s[i].isalpha():
                    ans += s[i]
                    i += 1
                elif s[i].isdigit():
                    n = 0
                    while s[i].isdigit():
                        n = 10*n + int(s[i])
                        i += 1
                    i += 1 # pass '['
                    subs, prevEnd = foo(s, i)
                    ans += subs * n
                    i = prevEnd + 1 # pass ']'
            return ans, i

        return foo(s, 0)[0]


    # Time:  O(n)
    # Space: O(n)
    def decodeString_stack3(self, s):  # hard to understand: curr[] append to strs[]
        curr, nums, strs = [], [], []
        n = 0

        for c in s:
            if c.isdigit():
                n = n * 10 + ord(c) - ord('0')
            elif c == '[':
                nums.append(n)
                n = 0
                strs.append(curr)
                curr = []
            elif c == ']':
                strs[-1].extend(curr * nums.pop())
                curr = strs.pop()
            else:
                curr.append(c)

        return "".join(strs[-1]) if strs else "".join(curr)

print(Solution().decodeString("3[a]2[bc]")) # "aaabcbc"
print(Solution().decodeString("3[a2[c]]")) # "accaccacc"
print(Solution().decodeString("2[abc]3[cd]ef")) # "abcabccdcdcdef"
