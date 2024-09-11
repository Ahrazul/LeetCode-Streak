# Problem: Maximum Average Subarray I
# Difficulty: Easy
# Runtime: 888 ms (Beats 55% of LeetCode users)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum = 0 

        for i in range(k):
            sum += nums[i]
        
        max_avg = sum / k

        for i in range(k,n):
            sum += nums[i]
            sum -= nums[i-k]
            avg = sum/k
            max_avg = max(avg, max_avg)
        
        return max_avg
