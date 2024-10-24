# Problem: Unique number of occurrences
# Difficulty: Medium
# Runtime: 4 ms (Beats 94% of LeetCode users)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ref = {}

        for i in arr:
            if i in ref.keys():
                ref[i] += 1
            else:
                ref[i] = 1
        
        lst = list(ref.values())

        if len(lst) == len(set(lst)):
            return True
        else:
            return False
        
