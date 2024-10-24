# Problem: Max number of k-sum pairs
# Difficulty: Medium
# Runtime: 498 ms (Beats 48% of LeetCode users)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        a=0
        l = 0
        r = len(nums) - 1 
        while l < r:
            if nums[l] + nums[r] == k:
                a += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else: 
                r -= 1
        return a    
