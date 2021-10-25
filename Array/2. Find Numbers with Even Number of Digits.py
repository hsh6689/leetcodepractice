"""
Given an array nums of integers, return how many of them contain an even number of digits.
 
Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 
Constraints:
1 <= nums.length <= 500, 1 <= nums[i] <= 10^5
"""

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        #loop thorugh the List, and check the length of the elemnt
        for num in nums:
            #check if the length is divisible by 2, which means even
            if(len(str(num))%2==0):
                ans+=1
        print("The total number of even number of digits is:",str(ans))
        return ans

test = [12,345,2,6,7896]
sol = Solution()
sol.findNumbers(test)