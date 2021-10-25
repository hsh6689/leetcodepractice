"""
Time complexity: O(N), since we are looping through enire array
space complexity: O(1), since we didnt allocate to another memory

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #use 2 pointers to iterate from the beginning of the array
        target=0
       
        if len(nums)==1:
            pass
        else:
            for i in range(len(nums)):
                #if nums[i] !=0, swap the values with target
                if nums[i]!=0:
                    #swap the values
                    nums[target], nums[i]= nums[i], nums[target]
                    target+=1