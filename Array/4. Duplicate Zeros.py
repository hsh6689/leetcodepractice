"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 
Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 9
"""

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        
        """
        #itr will store the position of iteration
        itr = 0
        arr_len = len(arr)
        
        #loop through the array
        while(itr<arr_len):
            #if the element is not 0, skip to next number
            if not arr[itr]:
                arr.pop()
                arr.insert(itr,0)
                itr+=1
            itr+=1
        print(arr)


test=[1,0,2,3,0,4,5,0]

#create Solution object and assign as 'sol'
sol=Solution()
#call function for test
sol.duplicateZeros(test)
                