# Time:  O(n^2)
# Space: O(n)

# 486
# Given an array of scores that are non-negative integers.
# Player 1 picks one of the numbers from either end of the array
# followed by the player 2 and then player 1 and so on.
# Each time a player picks a number, that number will not be available for the next player.
# This continues until all the scores have been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner.
# You can assume each player plays to maximize his score.
#
# Example 1:
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5.
# If player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return False.
# Example 2:
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7.
# No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
# Note:
# 1 <= length of the array <= 20.
# Any scores in the given array are non-negative integers and will not exceed 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.

class Solution(object):
    def PredictTheWinner(self, nums): # refer to conis-in-a-line case 3
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if the count of nums is even, player 1 can choose either all odd indices or all even indices, ganrantee to win.
        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True

        # dp is optimized from 2D list. In 2D dp[i,j] stores "player1's score minus player2's score" when there is nums[i:j+1] to choose.
        dp = [0] * n
        for i in reversed(range(n)):
            dp[i] = nums[i]
            for j in range(i+1, n):
                # when nums[i:j+1] available, either takes i and opponent choose from nums[i+1:j+1],
                # or takes j and opponent choose from nums[i:j]
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0

        '''
        # dp[rowId][j] is the most value first player can get when rowId to j coins left
        # space optmized, eventually rowId is 0
        dp = [0] * n
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        for i in reversed(range(n)):
            dp[i] = nums[i]
            for j in range(i+1, n):
                dp[j] = prefixSum[j+1] - prefixSum[i] - min(dp[j], dp[j-1])
        return dp[n-1] * 2 >= prefixSum[-1]

        '''


    def PredictTheWinner2(self, nums):
        """
        print the path of picking: don't save the path along the way, after dp 2-D
        array is filled, find the path which only takes O(n) time
        """
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for s in reversed(range(len(nums))):
            dp[s][s] = nums[s]
            for e in range(s+1, len(nums)):
                dp[s][e] = max(nums[s] - dp[s+1][e], nums[e] - dp[s][e-1])
        #print(dp)
        s, e, player1 = 0, len(nums)-1, True
        while s < e:
            if nums[s]-dp[s+1][e] >= nums[e]-dp[s][e-1]:
                pick = s
                s += 1
            else:
                pick = e
                e -= 1
            print("I" if player1 else "You", "take", nums[pick], "at", pick)
            player1 = not player1
        print("I" if player1 else "You", "take", nums[s], "at", s)

        return

    def PredictTheWinner3(self, nums):
        """
        print the index/numbers you should pick to win: Hard to understand by the following to store the path
        along the way to fill the 1-D array; better to modify PredictTheWinner2.
        """
        length = len(nums)
        dp, path = [0] * length, [[0]*length for _ in range(length)] # 1st list stores score, 2nd list stores selected indexes
        for s in reversed(range(len(nums))):
            dp[s] = nums[s]
            path[s][s] = 1
            for e in range(s+1, len(nums)):
                v1 = nums[s] - dp[e]
                v2 = nums[e] - dp[e-1]
                if v1 >= v2:
                    dp[e] = v1
                    path[e] = [-x for x in path[e]]
                    path[e][s] = 1
                else:
                    dp[e] = v2
                    path[e] = [-x for x in path[e-1]]
                    path[e][e] = 1
        print(path)
        return [i for i, x in enumerate(path[-1]) if x > 0]

    def PredictTheWinner_wrong(self, nums):
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True

        even = sum(nums[1::2])
        odd = sum(nums[2::2])
        if nums[0] + min(even, odd) >= max(even, odd):
            return True

        # wrong on [0,0,7,6,5,6,1]. After 1st player takes last elem 1, the 2nd player can take 6+0+7=13
        # Taking odd half (12) or even half (12) from [0,0,7,6,5,6] is just a strategy guaranteed to win,
        # but not the maximum can be taken from [0,0,7,6,5,6].
        even = sum(nums[0:-1:2])
        odd = sum(nums[1:-1:2])
        if nums[-1] + min(even, odd) >= max(even, odd):
            return True

        return False

print(Solution().PredictTheWinner([0,0,7,6,5,6,1])) # False
print(Solution().PredictTheWinner([3,2,2,3,1,2])) # True
print(Solution().PredictTheWinner([1,5,233,7])) # True
print(Solution().PredictTheWinner2([1,5,233,7])) # 222
print(Solution().PredictTheWinner3([1,5,233,7])) # [0, 2]
        
