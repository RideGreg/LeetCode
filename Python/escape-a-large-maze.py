# Time:  O(B^2)
# Space: O(B)

import collections


class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        R, C = 10**6, 10**6
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def bfs(blocks, source, target):
            max_area_surrounded_by_blocks = len(blocks)*(len(blocks)-1)//2
            lookup = set([source])
            if len(lookup) > max_area_surrounded_by_blocks:
                return True
            q = collections.deque([source])
            while q:
                source = q.popleft()
                if source == target:
                    return True
                for direction in directions:
                    cr, cc = source[0]+direction[0], source[1]+direction[1]
                    if not ((0 <= cr < R) and
                            (0 <= cc < C) and 
                            (cr, cc) not in lookup and
                            (cr, cc) not in blocks):
                        continue
                    lookup.add((cr, cc))
                    if len(lookup) > max_area_surrounded_by_blocks:
                        return True
                    q.append((cr, cc))
            return False
        
        return bfs(set(map(tuple, blocked)), tuple(source), tuple(target))
