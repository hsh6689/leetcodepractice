"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
 
Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #get the number of elements
        n=len(nums)
        #create a set with range[1,n]
        ans=set()
        for i in range(n):
            ans.add(i+1)
        #iterate thrugh the nums array and discard from ans
        #discard() removes element x from the set if the element is present.
        for num in nums:
            ans.discard(num)
            
        return ans