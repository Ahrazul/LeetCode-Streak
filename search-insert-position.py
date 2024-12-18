# Problem: Search Insert Position
# Difficulty: Easy
# Runtime: 49 ms (Beats 58% of LeetCode users)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end: 
            mid = (start + end) // 2
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target: 
                end = mid - 1
            else:
                start = start + 1
        return start 
