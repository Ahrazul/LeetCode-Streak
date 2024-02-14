# Problem: Reverse vowels of a string
# Difficulty: Easy
# Runtine: 65ms (Beats 44% of Leetcode users)

class Solution:
    def reverseVowels(self, s: str) -> str:
        def insert(l1, l2, indicator):
            j = 0
            for i in range(len(l1)):
                if l1[i] == indicator:
                    l1[i] = l2[j]
                    j += 1
            return l1
        def isVowel(s):
            if s == "A" or s == "E" or s == "I" or s == "O" or s == "U" or s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
                return True
        l1 = list(s)
        l2 = []
        for i in range(len(l1)):
            if isVowel(l1[i]):
                l2.append(l1[i])
                l1[i] = 0
        return "".join(insert(l1, l2[::-1], 0))
