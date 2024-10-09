# Problem: Maximum Number of Vowels in a Substring of Given Length
# Difficulty: Medium
# Runtime: 179 ms (Beats 66% of LeetCode users)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']
        l, result, count = 0, 0, 0
        for r in range(len(s)):
            if r - l + 1 > k:
                count -= 1 if s[l] in vowel else 0
                l += 1
                if s[r] in vowel:
                    count += 1
            else:
                if s[r] in vowel:
                    count += 1
            result = max(result, count)
        return result
