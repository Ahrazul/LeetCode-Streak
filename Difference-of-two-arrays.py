# Problem: Find the Difference of Two Arrays
# Difficulty: Easy
# Runtime: 9 ms (Beats 98% of LeetCode users)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        res1, res2 = set(), set()

        for i in range(len(nums1)):
            if nums1[i] not in set2:
                res1.add(nums1[i])
            
        for i in range(len(nums2)):
            if nums2[i] not in set1:
                res2.add(nums2[i])
        
        return [list(res1), list(res2)]
