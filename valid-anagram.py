# Problem Name: Valid Anagram
# Problem Difficulty: Easy
# Runtime: 55 ms (Beats 45% of LeetCode users)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_t = sorted(s)
        sorted_s = sorted(t)
        return sorted_s == sorted_t
