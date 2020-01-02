# Time:  O(nlogn)
# Space: O(n)

# 1200
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        result = []
        min_diff = float("inf")
        arr.sort()
        for i in xrange(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                result.append([arr[i], arr[i+1]])
        return result
        ''' Con: storing pairs with larger difference wastes space
        lookup, minKey = collections.defaultdict(list), float('inf')
        arr.sort()
        for i in range(len(arr)-1):
            x, y = arr[i], arr[i+1]
            if y-x <= minKey:
                lookup[y-x].append([x, y])
                minKey = min(minKey, y-x)
        return lookup[minKey]

        '''

    # TLE: O(n^2)
    def minimumAbsDifference_TLE(self, arr: List[int]) -> List[List[int]]:
        lookup, minKey = collections.defaultdict(list), float('inf')
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                x, y = arr[i], arr[j]
                lookup[abs(x-y)].append([min(x,y), max(x,y)])
                minKey = min(minKey, abs(x-y))
        return sorted(lookup[minKey])