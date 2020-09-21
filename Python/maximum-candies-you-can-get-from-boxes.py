# Time:  O(n^2)
# Space: O(n)

# 1298 weekly contest 168 12/21/2019

# Given n boxes, each box is given in the format [status, candies, keys, containedBoxes] where:
#
# status[i]: an integer which is 1 if box[i] is open and 0 if box[i] is closed.
# candies[i]: an integer representing the number of candies in box[i].
# keys[i]: an array contains the indices of the boxes you can open with the key in box[i].
# containedBoxes[i]: an array contains the indices of the boxes found in box[i].
# You will start with some boxes given in initialBoxes array. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.
#
# Return the maximum number of candies you can get following the rules above.

# Each box is contained in one box at most.
# 1 <= status.length <= 1000


import collections


class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        result = 0
        q = collections.deque(initialBoxes)
        while q:
            changed = False
            sz = len(q)
            for _ in range(sz):
                box = q.popleft()
                if not status[box]:
                    q.append(box)
                else:
                    changed = True
                    result += candies[box]
                    for contained_key in keys[box]:
                        status[contained_key] = 1
                    q.extend(containedBoxes[box])
            if not changed:
                break
        return result

    def maxCandies_ming(self, status, candies, keys, containedBoxes, initialBoxes):
        ans, cur, cont = 0, initialBoxes, True
        while cont:
            cont = False
            nxt = []
            for i in cur:
                if status[i]:
                    ans += candies[i]
                    nxt.extend(containedBoxes[i])
                    for k in keys[i]:
                        status[k] = 1
                    cont = True
                else:
                    nxt.append(i) # 没打开的box统统留到下次处理
            cur = nxt
        return ans

        '''
        #已经意识到一次处理不完，试图作第二次处理。其实仍然不够，应该无限次循环加个退出条件
        #key的作用就是改为open状态，维护myKey较麻烦，不如更新状态
        oBox, cBox, myKey = [], [], set()
        q = collections.deque(initialBoxes)
        while q:
            i = q.popleft()
            if status[i] or i in myKey:
                oBox.append(i)
                myKey.update(keys[i])
                for j in containedBoxes[i]:
                    q.append(j)
            else:
                cBox.append(i)
        oBox2, cBox2 = [], []
        q = collections.deque(oBox+cBox)
        while q:
            i = q.popleft()
            if status[i] or i in myKey:
                oBox2.append(i)
                myKey.update(keys[i])
            else:
                cBox2.append(i)

        return sum(candies[i] for i in oBox2)
        '''

print(Solution().maxCandies([1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0])) # 16
print(Solution().maxCandies([1,0,0,0,0,0], [1,1,1,1,1,1], [[1,2,3,4,5],[],[],[],[],[]],
                            [[1,2,3,4,5],[],[],[],[],[]], [0]))  # 6
print(Solution().maxCandies([1,1,1], [100,1,100], [[],[0,2],[]], [[],[],[]], [1])) # 1
print(Solution().maxCandies([1], [100], [[]], [[]], [])) # 0
print(Solution().maxCandies([1,1,1], [2,3,2], [[],[],[]], [[],[],[]], [2,1,0])) # 7
