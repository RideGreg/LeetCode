import collections
class Solution:
    """
    @param Maze:
    @return: nothing
    """
    def Portal(self, Maze):
        q = collections.deque()
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        r, c = len(Maze), len(Maze[0])
        cont = True
        for i in xrange(r):
            if cont:
                for j in xrange(c):
                    if Maze[i][j] == 'S':
                        q.append([i,j,0]);
                        cont = False
                        break
        while q:
            item = q.popleft()
            for dir in dirs:
                x, y = item[0]+dir[0], item[1]+dir[1]
                if 0<=x<r and 0<=y<c:
                    if Maze[x][y] == 'E':
                        return item[2]+1
                    elif Maze[x][y] == '*':
                        q.append([x,y,item[2]+1])
                        Maze[x][y] = '#'
        return -1
print Solution().Portal([
['S','*','E'],
['*','*','*'],
['#','*','*'],
['#','#','E']
]);