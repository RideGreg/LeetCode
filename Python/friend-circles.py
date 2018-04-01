# Time:  O(n^2)
# Space: O(n)

# There are N students in a class. Some of them are friends, while some are not.
# Their friendship is transitive in nature.
# For example, if A is a direct friend of B, and B is a direct friend of C,
# then A is an indirect friend of C.
# And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class.
# If M[i][j] = 1, then the ith and jth students are direct friends with each other,
# otherwise not. And you have to output the total number of friend circles among all the students.
#
# Example 1:
# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.
#
# Example 2:
# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
#
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

# https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
# http://blog.csdn.net/dm_vincent/article/details/7655764
# http://blog.csdn.net/dm_vincent/article/details/7769159

class Solution(object):
    def findCircleNum(self, M): # slowest, constructing class wastes time
        """
        :type M: List[List[int]]
        :rtype: int
        """
        class UnionFind(object):
            def __init__(self, n):
                self.set = range(n)
                self.count = n
        
            def find_set(self, x):
               if self.set[x] != x:
                   self.set[x] = self.find_set(self.set[x])  # path compression.
               return self.set[x]
        
            def union_set(self, x, y):
                x_root, y_root = map(self.find_set, (x, y))
                if x_root != y_root:
                    self.set[min(x_root, y_root)] = max(x_root, y_root)
                    self.count -= 1

        circles = UnionFind(len(M))
        for i in xrange(len(M)):
            for j in xrange(len(M)):
                if M[i][j] and i != j:
                    circles.union_set(i, j)
        return circles.count

class Solution_quick(object): # fastest, same logic as the above orig solution
    def findCircleNum(self, M):
        size = len(M)
        pid = range(size)

        def find(x):
            if pid[x] != x:
                pid[x] = find(pid[x])
            return pid[x]

        for i in xrange(size):
            for j in xrange(size):
                if i != j and M[i][j] == 1:
                    pi, pj = find(i), find(j)
                    if pi != pj:
                        pid[min(pi, pj)] = max(pi, pj)
                        size -= 1
        return size

 # bad: need to maintain the list of circles: take extra space and update is time consuming
class Solution_ming(object):
    def findCircleNum(self, M):
        lookup = [False] * len(M) # maintain a list of mapping friend to its circle Id
        circles = [] # maintain a list of set, each set is a circle
        size = 0
        for i in xrange(len(M)):
            for j in xrange(len(M[0])):
                if M[i][j] == 1:
                    if lookup[i] is False and lookup[j] is False: # create a new circle
                        circles.append(set([i, j]))
                        lookup[i] = lookup[j] = len(circles) - 1
                        size += 1
                    elif lookup[i] is not False and lookup[j] is not False: # merge circles
                        smallCId, bigCId = min(lookup[i], lookup[j]), max(lookup[i], lookup[j])
                        if smallCId != bigCId:
                            for k in circles[bigCId]:
                                lookup[k] = smallCId
                            circles[smallCId].update(circles[bigCId])
                            circles[bigCId] = set()
                            size -= 1
                    else: # add to existing circle
                        cId = lookup[i] if lookup[i] is not False else lookup[j]
                        circles[cId].update([i, j])
                        lookup[i] = lookup[j] = cId
        return size

#Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
#Solution().findCircleNum([[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])


#0.246370077133 sec
#0.0578229427338 sec
#0.096510887146 sec
import time
t = time.time()
for _ in xrange(10000):
    Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
print '{} sec'.format(time.time()-t)

t = time.time()
for _ in xrange(10000):
    Solution_quick().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
print '{} sec'.format(time.time()-t)

t = time.time()
for _ in xrange(10000):
    Solution_ming().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
print '{} sec'.format(time.time()-t)