# Time:  O(1) on average. Total time is O(q) for q queries made, as each timepoint is inserted/deleted once.
# Space: O(w), w = 3000 means the size of window we should scan. Can be considered as O(1) in this problem.

# 933 contest 109 11/3/2018
#
# Write a class RecentCounter to count recent requests.
# It has only one method: ping(int t), where t represents some time in milliseconds.
#
# Return the number of pings that have been made from 3000 milliseconds ago until now.
# Any ping with time in [t - 3000, t] will count, including the current ping.
#
# It is guaranteed that every call to ping uses a strictly larger value of t than before.
#
# Solution: only care about recent calls in last 3000ms. Calls occurred before t-3000 can be removed.
#           Test a proper data structure.

import collections


class RecentCounter(object):

    def __init__(self):
        self.__q = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.__q.append(t)
        while self.__q[0] < t-3000:
            self.__q.popleft()
        return len(self.__q)

obj = RecentCounter()
print(obj.ping(1)) # 1
print(obj.ping(100)) # 2
print(obj.ping(3001)) # 3
print(obj.ping(3002)) # 3