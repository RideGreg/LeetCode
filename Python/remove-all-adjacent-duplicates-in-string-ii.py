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
            if not stk or stk[-1][0] != c:
                stk.append([c, 1])
            else:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
        return "".join(c*k for c, k in stk)
        ''' OR
        ans = []
        for c,ct in stack:
            ans.extend([c] * ct)
        return "".join(ans)        
        '''

    # maintain repeated count for last element, need recount after pop
    # not good as the above to maintain repeated count for every element
    def removeDuplicates_ming(self, s, k):
        result, cnt = [], 0
        for c in s:
            if cnt == k-1 and c == result[-1]:
                result = result[:-(k-1)]
                if result:
                    cnt = 1
                    while cnt+1 <= len(result) and result[-cnt-1] == result[-cnt]:
                        cnt += 1
                else:
                    cnt = 0
            else:
                if result and result[-1] == c:
                    cnt += 1
                else:
                    cnt = 1
                result.append(c)
        return "".join(result)

print(Solution().removeDuplicates("abcd", 2)) # "abcd"
print(Solution().removeDuplicates("deeedbbcccbdaa", 3)) # "aa"
print(Solution().removeDuplicates("pbbcggttciiippooaais", 2)) # "ps"
