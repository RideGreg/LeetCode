# Time:  O(m * n)
# Space: O(n)

# 562
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.


# DP: 分表用二维数组h[x][y], v[x][y], d[x][y], a[x][y]表示以元素M[x][y]结尾，横向、纵向、主对角线、
# 反对角线连续1的最大长度
#
# 状态转移方程如下：
#
# h[x][y] = M[x][y] * (h[x][y - 1]  + 1)
#
# v[x][y] = M[x][y] * (v[x - 1][y]  + 1)
#
# d[x][y] = M[x][y] * (d[x - 1][y - 1]  + 1)
#
# a[x][y] = M[x][y] * (a[x - 1][y + 1]  + 1)

class Solution(object):
    def longestLine(self, M): # USE THIS: only traverse once, only depend on the row above
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M: return 0

        m, n, ans = len(M), len(M[0]), 0
        h = [[0] * n for _ in range(2)]
        v = [[0] * n for _ in range(2)]
        d = [[0] * n for _ in range(2)]
        a = [[0] * n for _ in range(2)]

        for i in range(m):
            for j in range(n):
                h[i%2][j] = M[i][j] * (h[i%2][j-1] + 1) if j > 0 else M[i][j]
                v[i%2][j] = M[i][j] * (v[(i+1)%2][j] + 1) if i > 0 else M[i][j]
                d[i%2][j] = M[i][j] * (d[(i+1)%2][j-1] + 1) if (i > 0 and j > 0) else M[i][j]
                a[i%2][j] = M[i][j] * (a[(i+1)%2][j+1] + 1) if (i > 0 and j < n-1) else M[i][j]
                ans = max(ans, h[i%2][j], v[i%2][j], d[i%2][j], a[i%2][j])
        return ans



    def longestLine_ming(self, M): # constant space, traverse four times
        m, n = len(M), len(M[0])
        # traverse horizontally
        hans = 0
        for i in range(m):
            v = 0
            for j in range(n):
                v = M[i][j] * (v + 1)
                hans = max(hans, v)
        # traverse vertically
        vans = 0
        for j in range(n):
            v = 0
            for i in range(m):
                v = M[i][j] * (v + 1)
                vans = max(vans, v)
        # traverse diagonally
        dans = 0
        for r in range(1-m, n):
            v = 0
            for i in range(max(0, -r), min(m-1, n-1-r)+1):
                j = i + r
                v = M[i][j] * (v + 1)
                dans = max(dans, v)
        # traverse anti-diagonally
        adans = 0
        for r in range(0, m+n-1):
            v = 0
            for i in range(max(0, r-(n-1)), min(m-1, r)+1):
                j = r - i
                v = M[i][j] * (v + 1)
                adans = max(adans, v)

        return max(hans, vans, dans, adans)

''' another example how to traverse in 4 directions
public class Solution {
    public int longestLine(int[][] M) {
        if (M.length == 0)
            return 0;
        int ones = 0;
        //horizontal
        for (int i = 0; i < M.length; i++) {
            int count = 0;
            for (int j = 0; j < M[0].length; j++) {
                if (M[i][j] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //vertical
        for (int i = 0; i < M[0].length; i++) {
            int count = 0;
            for (int j = 0; j < M.length; j++) {
                if (M[j][i] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //upper diagonal
        for (int i = 0; i < M[0].length || i < M.length; i++) {
            int count = 0;
            for (int x = 0, y = i; x < M.length && y < M[0].length; x++, y++) {
                if (M[x][y] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //lower diagonal
        for (int i = 0; i < M[0].length || i < M.length; i++) {
            int count = 0;
            for (int x = i, y = 0; x < M.length && y < M[0].length; x++, y++) {
                if (M[x][y] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //upper anti-diagonal
        for (int i = 0; i < M[0].length || i < M.length; i++) {
            int count = 0;
            for (int x = 0, y = M[0].length - i - 1; x < M.length && y >= 0; x++, y--) {
                if (M[x][y] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //lower anti-diagonal
        for (int i = 0; i < M[0].length || i < M.length; i++) {
            int count = 0;
            for (int x = i, y = M[0].length - 1; x < M.length && y >= 0; x++, y--) {
                //System.out.println(x+" "+y);
                if (M[x][y] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        return ones;

    }
}
'''

    def longestLine_bookshadow(self, M):
        m, n = len(M), len(M) and len(M[0]) or 0
        ans = 0

        #horizontal & diagonal
        diag = [[0] * n for _ in range(m)]
        for i in range(m):
            cnt = 0
            for j in range(n):
                cnt = M[i][j] * (cnt + 1)
                diag[i][j] = M[i][j]
                if i > 0 and j > 0:
                    diag[i][j] = M[i][j] * (diag[i - 1][j - 1] + 1)
                ans = max(ans, cnt, diag[i][j])

        #vertical & anti-diagonal
        adiag = [[0] * n for _ in range(m)]
        for j in range(n):
            cnt = 0
            for i in range(m):
                cnt = M[i][j] * (cnt + 1)
                adiag[i][j] = M[i][j]
                if i < m - 1 and j > 0:
                    adiag[i][j] = M[i][j] * (adiag[i + 1][j - 1] + 1)
                ans = max(ans, cnt, adiag[i][j])

        return ans


print(Solution().longestLine([
    [0,1,1,0],
    [0,1,1,0],
    [0,0,0,1]
])) # 3

print(Solution().longestLine([
    [0,1,1,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,1,0,1],
    [0,0,0,1]
])) # 3
