# Time:  O(n)
# Space: O(1)

# 1441
# Given an array target and an integer n. In each iteration, you will read a number 
# from  list = {1,2,3..., n}.

# Build the target array using the following operations:
# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

# Return the operations to build the target array. You are guaranteed that the answer is unique.


class Solution(object):
    def buildArray(self, target, n): # USE THIS: scan target array takes much less steps than scan [1, n]
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result, curr = [], 1
        for t in target:
            result.extend(["Push", "Pop"]*(t-curr))
            result.append("Push")
            curr = t+1
        return result


    def buildArray(self, target, n):
        i, ans = 0, []
        for start in range(1, n+1):
            ans.append('Push')
            if start < target[i]:
                ans.append('Pop')
            elif start == target[i]:
                i += 1
                if i >= len(target):
                    break
        return ans

print(Solution().buildArray([1, 3], 3)) # ["Push","Push","Pop","Push"]