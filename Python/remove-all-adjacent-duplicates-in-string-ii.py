# Time:  O(n)
# Space: O(n)

# 1209
# Given a string s, a k duplicate removal consists of choosing k adjacent and equal
# letters from s and removing them causing the left and the right side of the deleted
# substring to concatenate together.
#
# We repeatedly make k duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made.
#
# It is guaranteed that the answer is unique.

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stk = []
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append([c, 1])
        return "".join(c*k for c, k in stk)


print(Solution().removeDuplicates("abcd", 2)) # "abcd"
print(Solution().removeDuplicates("deeedbbcccbdaa", 3)) # "aa"
print(Solution().removeDuplicates("pbbcggttciiippooaais", 2)) # "ps"
