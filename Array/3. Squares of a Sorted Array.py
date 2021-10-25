"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #first, sort the array by absoluting the elements
        ans_Nums=sorted(nums,key=abs)
        #Second, loop thorugh the array and square the numbers
        ans_Nums = (number ** 2 for number in ans_Nums)

        ans = list(ans_Nums)
        print("Sqaured nums:", ans)
        return ans

test=[-4,-1,0,3,10]

#create Solution object and assign as 'sol'
sol=Solution()
#call function for test
sol.sortedSquares(test)