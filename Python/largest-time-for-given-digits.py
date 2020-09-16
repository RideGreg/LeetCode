# Time:  O(1)
# Space: O(1)

# 949
# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00,
# a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

import itertools


class Solution(object):
    def largestTimeFromDigits(self, A): # USE THIS
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort(reverse=True) # optimization for early return
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10*h1 + h2
            mins = 10*m1 + m2
            if 0 <= hours < 24 and 0 <= mins < 60:
                return "{:02}:{:02}".format(hours, mins)
        return ''

    # backtracking to generate own permutation, compare every possible time string.
    def largestTimeFromDigits_backtrack(self, A):
        def backtrack(cur):
            if len(cur) == 4:
                perm.append(cur[:])
            else:
                for i in range(4):
                    if not used[i]:
                        used[i] = True
                        cur.append(A[i])
                        backtrack(cur)
                        cur.pop()
                        used[i] = False

        mx, ans = -1, None
        used = [False] * 4
        perm = []
        backtrack([])
        for B in perm:
            h = 10*B[0] + B[1]
            m = 10*B[2] + B[3]
            if 0 <= h < 24 and 0 <= m < 60 and 60*h+m > mx:
                mx, ans = 60*h+m, B
        return "{}{}:{}{}".format(ans[0],ans[1],ans[2],ans[3]) if mx != -1 else ''


    # VERY HARD to write code for picking up valid digits for each place. And the following
    # is still wrong which returns '' for [2,0,6,6] (tried to make '20:xx')
    def largestTimeFromDigits_wrong(self, A):
        h, m = '', ''
        if 2 not in A and 1 not in A and 0 not in A:
            return ''
        if 2 in A:
            h = '2'
            A.remove(2)
            if 3 not in A and 2 not in A and 1 not in A and 0 not in A:
                return ''
            if 3 in A:
                h = '23:'
                A.remove(3)
            elif 2 in A:
                h = '22:'
                A.remove(2)
            elif 1 in A:
                h = '21:'
                A.remove(1)
            elif 0 in A:
                h = '20:'
                A.remove(0)
        elif 1 in A:
            h = '1'
            A.remove(1)
        elif 0 in A:
            h = '0'
            A.remove(0)

        less6 = []
        for a in A:
            if a <= 5: less6.append(a)
        if len(less6) == 0:
            return ''
        elif len(less6) == 1:
            m = str(less6[0])
            A.remove(less6[0])
            if len(A) == 2:
                return h+str(max(A))+':'+m+str(min(A))
            else:
                return h+m+str(A[0])
        else:
            A.sort()
            if len(A) == 3:
                return h+str(A[2])+':'+str(A[1])+str(A[0])
            else:
                return h+str(A[1])+str(A[0])

print(Solution().largestTimeFromDigits([2,0,6,6])) # 06:26
print(Solution().largestTimeFromDigits([1,2,3,4])) # 23:41
print(Solution().largestTimeFromDigits([5,5,5,5])) # ''
print(Solution().largestTimeFromDigits([1,6,3,9])) # 19:36
print(Solution().largestTimeFromDigits([1,5,3,9])) # 19:53
print(Solution().largestTimeFromDigits([3,2,7,0])) # 23:07