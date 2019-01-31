# Time:  O(n)
# Space: O(n)

# 946
# Given two sequences pushed and popped with distinct values, return true if and only if this could have been the
# result of a sequence of push and pop operations on an initially empty stack.

# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.

# Solution: Greedy
# We have to push the items in order. Greedily pop values from top of stack if they are
# the next values to pop.

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j = 0
        s = []
        for v in pushed:
            s.append(v)
            while s and s[-1] == popped[j]:
                s.pop()
                j += 1
        return j == len(popped)

    def validateStackSequences_ming(self, pushed, popped):
        n, i, j = len(pushed), 0, 0
        stk = []
        while i < n or j < n:
            if stk and stk[-1] == popped[j]: # greedily pop
                stk.pop()
                j += 1
            else:
                if i < n:
                    stk.append(pushed[i])
                    i += 1
                else:
                    break
        return not stk and i == n and j == n

print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])) # True
print(Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])) # False
