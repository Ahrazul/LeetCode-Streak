# Problem: Is Subsequence
# Difficulty: Easy
# Runtime: 22 ms (Beats 99.46% of LeetCode users)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a, b = 0, 0 
        while a < len(s) and b < len(t):
            if s[a] == t[b]:
                a += 1
            b += 1
        return True if a == len(s) else False
