# Time:  set: O(1)
#        get: O(logn)
# Space: O(n)

# 981
# Create a timebased key-value store class TimeMap, that supports two operations.
#
# 1. set(string key, string value, int timestamp)
# Stores the key and value, along with the given timestamp.

# 2. get(string key, int timestamp)
# Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the one with the largest timestamp_prev.
# If there are no values, it returns the empty string ("").

# Input: inputs = ["TimeMap","set","get","get","set","get","get"],
#        inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]

import collections
import bisect


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.lookup[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        A = self.lookup.get(key, None)
        if A is None:
            return ""
        i = bisect.bisect_right(A, (timestamp+1, 0))
        return A[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
