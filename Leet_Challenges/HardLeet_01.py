# *** LeetCode Challenge - Hard Level ***
# Median of Two Sorted Arrays
# Hard
# Topics
# premium lock icon
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


## Code:

class Solution(object):
    def find_median_sorted_array(self, nums1, nums2):

        new_nums = nums1 + nums2
        new_nums.sort()
        n_length = len(new_nums)

        # checking if we had to find the median of an even or odd length array

        if n_length % 2 == 0:
            median = (new_nums[n_length // 2 - 1] + new_nums[n_length // 2]) / 2.0
        else:
            median = new_nums[n_length // 2]
        
        return median

# Example of the Solution

sol_class = Solution()
result = sol_class.find_median_sorted_array([1, 3], [2])            
print(result)