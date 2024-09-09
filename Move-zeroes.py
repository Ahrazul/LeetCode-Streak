# Problem: Move Zeroes
# Difficulty: Easy
# Runtime: 122 ms (Beats 92% of LeetCode users)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0 
        temp = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l += 1
        return nums 
