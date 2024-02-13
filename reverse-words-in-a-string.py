# Problem: Reverse words in a string 
# Difficulty: Medium
# Runtine: 33ms (Beats 84% of Leetcode users)

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l1 = s.split()
        l1 = l1[::-1]
        var = ''
        for i in range(len(l1)):
            var = var + ' ' + l1[i]
        return var[1:]
