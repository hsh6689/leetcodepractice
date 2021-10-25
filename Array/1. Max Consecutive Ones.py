"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #ans will store the size of consecutive 1 
        ans=0
        #temp will temporaily store the size of consecutive 1
        temp=0

        #loop through the list
        for index, elem in enumerate(nums):
            curr_el = int(nums[index])
            #if current element is 1, increment temp
            if curr_el == 1:
                temp+=1
                #compare beteen previously stored value and store higher val
                if(ans<temp):
                    ans=temp
            else:
                temp=0
        print("The maximum number of consecutive 1's in this arry is",str(ans) )
        return ans

test=[1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1]

#create Solution object and assign as 'sol'
sol=Solution()
#call function for test
sol.findMaxConsecutiveOnes(test)