# Problem: Increasing Triplet Subsequence 
# Difficulty: Medium
# Runtime: 400 ms (Beats 55% of LeetCode users)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        leftmin = [nums[0]]
        var = nums[::-1]
        rightmax = [var[0]]
        for i in range(1, len(nums)):
            if nums[i] < leftmin[i-1]:
                leftmin.append(nums[i])
            else: 
                leftmin.append(leftmin[i-1])
        for j in range(1, len(var)):
            if var[j] > rightmax[j-1]:
                rightmax.append(var[j])
            else:
                rightmax.append(rightmax[j-1])
        rightmax = rightmax[::-1]
        for k in range(len(nums)):
            if leftmin[k] < nums[k] and rightmax[k] > nums[k]:
                return True
        return False
