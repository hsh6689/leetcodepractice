"""
Reference:https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common=strs[0]
      
        for j in range(1,len(strs)):
            temp_str=strs[j]            
            
            if common=="":
                return common
            
            for i in range(len(common)):
                if i<len(temp_str) and common[i]==temp_str[i]:
                    continue
                else:
                    common=common[0:i]
                    break

        return common