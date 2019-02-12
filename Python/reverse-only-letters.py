# Time:  O(n)
# Space: O(1)

# 917
# Given a string S, return the "reversed" string where
# all characters that are not a letter stay in the same place,
# and all letters reverse their positions.
#
# Example 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
# Note:
# - S.length <= 100
# - 33 <= S[i].ASCIIcode <= 122 
# - S doesn't contain \ or "

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # USE THIS: two pointers, only one pass
        i, j = 0, len(S)-1
        A = list(S)
        while i<j:
            while i<j and not A[i].isalpha():
                i += 1
            while i<j and not A[j].isalpha():
                j -= 1
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return ''.join(A)

    def reverseOnlyLetters_kamyu(self, S):
        def getNext(S):
            for i in reversed(xrange(len(S))):
                if S[i].isalpha():
                    yield S[i]

        result = []
        letter = getNext(S)
        for i in xrange(len(S)):
            if S[i].isalpha():
                result.append(letter.next())
            else:
                result.append(S[i])
        return "".join(result)

    def reverseOnlyLetters_stack(self, S): # similar to the above generator solution, but take stack SPACE
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)