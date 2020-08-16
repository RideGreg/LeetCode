# Time:  O(n)
# Space: O(1)

# 41
# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.
#

# Method 1. 答案一定在[1, n+1]范围内，先遍历所给数组填哈希表，再次遍历哈希表找所缺的数。需要额外空间
# Method 2. 排序再遍历，找到不连续的数。超过O(n)
# Method 3. 正确做法：原地交换法：排好序应该是[1,2,...n];遍历，如果数k不在[1, n]范围，不管，看下一个；
#    如果k在[1, n]内，换到该去的位置k-1；继续检查换进来的数。交换完所有可交换的以后，遍历找出缺的数。
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(len(A)):
            # 如果1<=此数<=len(A),持续把它换到应属位置上去。假设数值为A[i]，应去位置A[i]-1，现在位置i。
            # KENG 1: 注意不能比较index while 1 <= A[i] <= len(A) and A[i] != i+1: 位置虽不同但数值相同，陷入死循环。 Eg. [1,1]
            while 1 <= A[i] <= len(A) and A[i] != A[A[i]-1]:
                x = A[i] - 1
                A[i], A[x] = A[x], A[i]
                # A[A[i] - 1], A[i] = A[i], A[A[i] - 1]  # this works, but better to avoid confusion
                # A[i], A[A[i] - 1] = A[A[i] - 1], A[i]  # KENG 2: not work, A[i] already updated

        for i, x in enumerate(A):
            if x != i + 1:
                return i + 1
        return len(A) + 1     # KENG 3: dont forget this


    def firstMissingPositive_similar(self, A): # similar but while iterate on the outside loop
        i = 0
        while i < len(A):
            x = A[i]
            if 1 <= x <= len(A) and A[i] != A[x - 1]:
                A[x-1], A[i] = A[i], A[x-1]
            else:
                i += 1

        for i, x in enumerate(A):
            if x != i + 1:
                return i + 1
        return len(A) + 1

if __name__ == "__main__":
    print(Solution().firstMissingPositive([3,4,-1,1])) # 2
    print(Solution().firstMissingPositive([1,1])) # 2
    print(Solution().firstMissingPositive([4,1,2,6])) # 3
    print(Solution().firstMissingPositive([1,8,0])) # 2
    print(Solution().firstMissingPositive([0,8,1])) # 2
    print(Solution().firstMissingPositive([2,1,0])) # 3
    print(Solution().firstMissingPositive([1,2,0])) # 3
    print(Solution().firstMissingPositive([])) # 1
    print(Solution().firstMissingPositive([0])) # 1
    print(Solution().firstMissingPositive([1])) # 2
    print(Solution().firstMissingPositive([2])) # 1
    print(Solution().firstMissingPositive([7,8,9,11,12])) # 1
