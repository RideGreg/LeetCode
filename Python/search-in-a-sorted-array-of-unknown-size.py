'''
Given a sorted array of unknown length and a number to search for, return the index of the number in the array. Accessing an element out of bounds throws exception. If the number occurs multiple times, return the index of any occurrence. If it isn’t present, return -1.

int a[] = {1,2,3,4,5,6,7,8};
Find Value: 6

Return: 5 (index number of value 6)

Time Complexity: O(logn)
Space Complexity: O(1)

public static int findNumberInSortedArrayWithoutArrayLength(int arr[], int findNo) {
	if(arr == null) return -1;
	
	int startIdx = 0, endIdx = 1, midIdx = 0;
	do {
		midIdx = (startIdx + endIdx )/2;
		try {
			if(arr[midIdx] == findNo) 
				return midIdx;
		}catch(ArrayIndexOutOfBoundsException e) {
			endIdx = midIdx-1;
			continue;
		}
		
		if(arr[midIdx] < findNo) {
			startIdx = midIdx + 1;
			try {
				if(arr[endIdx]>findNo)
					endIdx --;
				else
					endIdx *= 2;
			}catch(ArrayIndexOutOfBoundsException e) {
				endIdx --;
			}
		}else {
			endIdx = midIdx - 1;
		}
	}while(startIdx<=endIdx);
	return -1;
}
'''
