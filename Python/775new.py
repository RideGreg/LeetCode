class Solution(object):
    def isIdealPermutation(self, A):

        l, g, cnt = 0, 0, 0
        for i, n in enumerate(A):
            if i < len(A)-1 and n > A[i+1]:
                l += 1
            if i != n:

                g += abs(n-i)
                cnt += 1
        print l, g, cnt, g-(cnt+1)/2
        return l == g-(cnt+1)/2
    '''
class Solution {
public:
    //from lihuoran python, shancha c++
    public boolean isIdealPermutation(int[] A) {
        int localRe = 0;
        for (int i = 0; i < A.length -1; i++) {
            if (A[i] > A[i+1]) localRe++;
        }

        int globalRe = mergeSort(A, 0, A.length);
        return globalRe == localRe;
    }

    private int mergeSort(int[] nums, int l, int r) {
        if (l + 1 >= r) return 0;
        int mid = l + (r - l) / 2;
        int cnt = mergeSort(nums, l, mid);
        cnt += mergeSort(nums, mid, r);
        int[] tmpNums = new int[r-l];

        int i = l;
        int j = mid;
        int t = mid;
        int k = 0;
        while (i < mid) {
            while (j < r && nums[i] < (long)nums[j]) j++;
            while (t < r && nums[i] < nums[t]) tmpNums[k++] = nums[t++];
            cnt += r - j;
            tmpNums[k++] = nums[i++];
        }
        System.arraycopy(tmpNums, 0, nums, l, k);
        return cnt;
    }
    bool isIdealPermutation(vector<int>& A) {
        for (int i = 0; i < A.size(); ++i) {
            if (A[i] != i) {
                if ((A[i] != i + 1) || (A[i+1] != i)) {
                    return false;
                } else {
                    ++i;
                }
            }
        }
        return true;
    }
    bool isIdealPermutation(vector<int>& A) {
        for (int i = 2, ma = A[0]; i < A.size(); ++i)
        {
            if (A[i] < ma)
                return false;
            ma = max(ma, A[i - 1]);
        }
        return true;
    }
};    
    '''

print Solution().isIdealPermutation([0,5,2,3,4,1,6])

print Solution().isIdealPermutation([1,0,2])
print Solution().isIdealPermutation([1,2,0])
