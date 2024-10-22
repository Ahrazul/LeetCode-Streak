# Problem: Longest Subarray of 1's after deleting one element
# Difficulty: Medium
# Runtime: 73 ms (Beats 97.48% of LeetCode users)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0 
        max_w = 0
        zero_count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            window = r - l 
            max_w = max(max_w, window)
        
        return max_w
