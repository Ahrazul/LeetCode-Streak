# Problem: Max Consecutive Ones III
# Difficulty: Medium
# Runtime: 71 ms (Beats 99% of LeetCode users)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zero_count = 0 
        max_w = 0 
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            
            w_size = r-l+1
            max_w = max(w_size,max_w)
        return max_w
