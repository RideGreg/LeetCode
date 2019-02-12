# Time:  ctor: O(n)
#        q:    O(logn)
# Space: O(n)
   
# 911
# In an election, the i-th vote was cast for persons[i] at time times[i].
#
# Now, we would like to implement the following query function:
# TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  
#
# Votes cast at time t will count towards our query. 
# In the case of a tie, the most recent vote (among tied candidates) wins.
#
# Example 1:
#
# Input: ["TopVotedCandidate","q","q","q","q","q","q"],
#        [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation: 
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
#
# Note:
# - 1 <= persons.length = times.length <= 5000
# - 0 <= persons[i] <= persons.length
# - times is a strictly increasing array with all elements in [0, 10^9].
# - TopVotedCandidate.q is called at most 10000 times per test case.
# - TopVotedCandidate.q(int t) is always called with t >= times[0].

import collections
import itertools
import bisect


class TopVotedCandidate(object):
    # USE THIS: no need to store each vote time; only store the time where leader changes
    # bisect 2nd param must be inf, so it is larger than the entry of same t.
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.__lookup = []
        count = collections.defaultdict(int)
        lead = -1
        for t, p in itertools.izip(times, persons):
            count[p] += 1
            if p != lead and count[p] >= count[lead]:
                lead = p
                self.__lookup.append((t, lead))

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        pos = bisect.bisect(self.__lookup, (t, float("inf")))
        return self.__lookup[pos-1][1]



# Ming solution: store all vote times, waste space; query needs to scan all candidates, waste time
import collections, itertools, bisect
class TopVotedCandidate_ming(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.cand = collections.defaultdict(list)
        for p, t in itertools.izip(persons, times):
            self.cand[p].append(t)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        ans = [-1, -1, -1]
        for c, times in self.cand.items():
            pos = bisect.bisect(times, t)
            if pos > 0:
                ans = max(ans, (pos, times[pos - 1], c))
        return ans[2]

# Your TopVotedCandidate object will be instantiated and called as such:
obj = TopVotedCandidate([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])
print(obj.q(3)) # 0
print(obj.q(12)) # 1
print(obj.q(25)) # 1
print(obj.q(15)) # 0
print(obj.q(24)) # 0
print(obj.q(8)) # 1
