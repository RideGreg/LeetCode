"""
Consider a big party where a log register for guest’s entry and exit times is maintained. 
Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.

Input: arrl[] = {1, 2, 9, 5, 5}
       exit[] = {4, 5, 12, 9, 12}
First guest in array arrives at 1 and leaves at 4, 
second guest arrives at 2 and leaves at 5, and so on.

Output: 5
There are maximum 3 guests at time 5. 
"""

class Solution:
    # O(max(n, max(start), max(end)))

    def maxOverlap(start, end):
        n = len(start)
        maxa = max(start)  # Finding maximum starting time
        maxb = max(end)  # Finding maximum ending time
        maxc = max(maxa, maxb)
        x = (maxc + 2) * [0]
        cur = 0;
        idx = 0

        for i in range(0, n):  # CREATING AN AUXILIARY ARRAY
            x[start[i]] += 1  # Lazy addition
            x[end[i] + 1] -= 1

        maxy = -1
        # Lazily Calculating value at index i
        for i in range(0, maxc + 1):
            cur += x[i]
            if maxy < cur:
                maxy = cur
                idx = i
        print("Maximum value is: {0:d}".format(maxy),
              " at position: {0:d}".format(idx))

"""
    An Efficient Solution is to use sorting n O(nLogn) time. The idea is to consider all events (all arrivals and exits) 
    in sorted order. Once we have all events in sorted order, we can trace the number of guests at any time keeping track of guests that have arrived, but not exited.
<?php 
// PHP Program to find maximum  
// guest at any time in a party 
  
function findMaxGuests($arrl, $exit, $n) 
{ 
      
    // Sort arrival and exit arrays 
    sort($arrl); 
    sort($exit); 
      
    // guests_in indicates number 
    // of guests at a time 
    $guests_in = 1;  
    $max_guests = 1;  
    $time = $arrl[0];  
    $i = 1; 
    $j = 0; 
      
    // Similar to merge in merge 
    // sort to process all events  
    // in sorted order 
    while ($i < $n and $j < $n) 
    { 
          
        // If next event in sorted 
        // order is arrival, 
        // increment count of guests 
        if ($arrl[$i] <= $exit[$j]) 
        { 
            $guests_in++; 
      
            // Update max_guests if needed 
            if ($guests_in > $max_guests) 
            { 
                $max_guests = $guests_in; 
                $time = $arrl[$i]; 
            } 
              
            // increment index of  
            // arrival array 
            $i++;  
        } 
          
        // If event is exit, decrement 
        // count of guests. 
        else 
        {                              
            $guests_in--; 
            $j++; 
        } 
    } 
      
    echo "Maximum Number of Guests = " , $max_guests
                               , " at time " , $time; 
} 
"""