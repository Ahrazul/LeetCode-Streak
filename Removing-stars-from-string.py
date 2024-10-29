# Problem: Removing stars from a string
# Difficulty: Medium
# Runtime: 91 ms (Beats 61% of LeetCode users)

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                stack and stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
