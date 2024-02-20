# Problem name: Length of Last Word
# Problem difficulty: Easy
# Runtime: 32 ms (Beats 90% of LeetCode Users)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if " " not in s:
            return len(s)
        else:
            return len(s.split()[-1])
