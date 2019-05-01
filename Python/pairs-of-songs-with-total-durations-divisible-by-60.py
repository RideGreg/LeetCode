# Time:  O(n)
# Space: O(1)

# 1010
# In a list of songs, the i-th song has a duration of time[i] seconds.
#
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.  Formally, we want the number of indices i < j with
# (time[i] + time[j]) % 60 == 0.
#
# Example 1:
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.

import collections

class Solution(object):
    # learn 1: to count each pair only once, do it progressively
    # learn 2: Note -t % 60 !== 60 - t % 60 when t is 0
    def numPairsDivisibleBy60(self, time): # USE THIS
        """
        :type time: List[int]
        :rtype: int
        """
        result = 0
        count = collections.Counter()
        for t in time:
            result += count[-t%60]
            count[t%60] += 1
        return result

    def numPairsDivisibleBy60_ming(self, time): # wordy than the above solution
        import collections
        count = collections.Counter(map(lambda x: x%60, time))
        ans = 0
        for k,v in count.items():
            if k == 0 or k == 30:
                ans += v*(v-1)//2
            elif k < 30:
                ans += v * count[60 - k]
        return ans
