# Time:  O(n)
# Space: O(n)

# 838 weekly contest 85 5/19/2018

# There are N dominoes in a line, and we place each domino vertically upright.
#
# In the beginning,
# we simultaneously push some of the dominoes either to the left or
# to the right.
#
# After each second,
# each domino that is falling to the left pushes the adjacent domino
# on the left.
#
# Similarly, the dominoes falling to the right push their adjacent dominoes
# standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides,
# it stays still due to the balance of the forces.
#
# For the purposes of this question,
# we will consider that a falling domino expends no additional force to a
# falling or already fallen domino.
#
# Given a string "S" representing the initial state. S[i] = 'L',
# if the i-th domino has been pushed to the left; S[i] = 'R',
# if the i-th domino has been pushed to the right; S[i] = '.',
# if the i-th domino has not been pushed.
#
# Return a string representing the final state.
#
# Example 1:
#
# Input:  ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
# Example 2:
#
# Input:  "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force
# on the second domino.
# Note:
# - 0 <= N <= 10^5
# - String dominoes contains only 'L', 'R' and '.'

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        force = [0]*len(dominoes)

        f = 0
        for i in xrange(len(dominoes)):
            if dominoes[i] == 'R':
                f = len(dominoes)
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f

        f = 0
        for i in reversed(xrange(len(dominoes))):
            if dominoes[i] == 'L':
                f = len(dominoes)
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f == 0 else 'R' if f > 0 else 'L'
                       for f in force)


    def pushDominoes_ming(self, dominoes):
        dominoes = list(dominoes)
        i, leftStart = 0, 0
        while i < len(dominoes):
            while i < len(dominoes) and dominoes[i] == '.':
                i += 1
            if i < len(dominoes):
                if dominoes[i] == 'L':
                    dominoes[leftStart:i+1] = 'L'*(i+1-leftStart)
                    i += 1
                    leftStart = i
                elif dominoes[i] == 'R':
                    j = i + 1
                    while j < len(dominoes) and dominoes[j] == '.':
                        j += 1
                    if j == len(dominoes) or dominoes[j] == 'R':
                        dominoes[i:j] = 'R' * (j-i)
                        i = j
                    elif dominoes[j] == 'L':
                        half = (j+1-i) // 2
                        dominoes[i:i+half] = 'R' * half
                        dominoes[j+1-half:j+1] = 'L' * half
                        i = j + 1
                        leftStart = i
        return ''.join(dominoes)

print(Solution().pushDominoes(".L.R...LR..L..")) # "LL.RR.LLRRLL.."
print(Solution().pushDominoes("RR.L")) # "RR.L"
