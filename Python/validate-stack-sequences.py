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
        stk = []
        for v in pushed:
            stk.append(v)
            while stk and stk[-1] == popped[j]:
                stk.pop()
                j += 1
        return j == len(popped) # ideally should be all popped


print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])) # True
print(Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])) # False
