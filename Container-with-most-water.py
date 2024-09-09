# Problem: Container with Most Water
# Difficulty: Medium
# Runtime: 519 ms (Beats 66% of LeetCode users)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        temp = 0 
        l, r = 0, len(height)-1
        while l < r:
            area = (r-l) * min(height[r], height[l])
            temp = max(temp, area)

            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return temp
        
