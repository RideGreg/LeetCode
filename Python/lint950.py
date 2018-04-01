'''
Given a 3 x 3 matrix, the number is 1~9, among which 8 squares have numbers, 1~8, and one is null (indicated by 0), asking if the corresponding number can be put on the corresponding label In the grid (spaces can only be swapped with up, down, left, and right positions), if it can output "YES", otherwise it outputs "NO".

Given matrix =
[
[1,2,3],
[4,0,6],
[7,5,8]
]
，return "YES"。

[[4,3,2],[5,0,8],[6,1,7]] return "NO"
'''

class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """
    def jigsawPuzzle(self, matrix):
        def move(n):
            dest = [(n-1)/3, (n-1)%3]
            for i in xrange(3):
                for j in xrange(3):
                    if matrix[i][j] == n:
                        cur = [i, j]
            while cur != dest:
                cx, cy = cur
                dx, dy = dest
                if cy < dy:
                    matrix[cx][cy], matrix[cx][cy+1] = matrix[cx][cy+1], matrix[cx][cy]
                    cur = [cx, cy+1]
                elif cy > dy:
                    matrix[cx][cy], matrix[cx][cy-1] = matrix[cx][cy-1], matrix[cx][cy]
                    cur = [cx, cy-1]
                elif cx < dx:
                    matrix[cx][cy], matrix[cx+1][cy] = matrix[cx+1][cy], matrix[cx][cy]
                    cur = [cx+1, cy]
                elif cx > dx:
                    matrix[cx][cy], matrix[cx-1][cy] = matrix[cx-1][cy], matrix[cx][cy]
                    cur = [cx-1, cy]
        for i in xrange(1, 7):
            print matrix
            move(i)
        print matrix
        return 'YES' if matrix[2] in ([0,7,8], [7,0,8], [7,8,0]) else 'NO'

print Solution().jigsawPuzzle([[4,3,2],[5,0,8],[6,1,7]])

print Solution().jigsawPuzzle([
[1,2,3],
[4,0,6],
[7,5,8]
])

