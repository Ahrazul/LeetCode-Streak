# Problem: Determine if two strings are close
# Difficulty: Medium
# Runtime: 90 ms (Beats 66% of LeetCode users)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}

        if len(word1) != len(word2):
            return False

        else:
            for i in word1:
                if i in d1.keys():
                    d1[i] += 1
                else:
                    d1[i] = 1
            
            for j in word2:
                if j in d2.keys():
                    d2[j] += 1
                else:
                    d2[j] = 1

            lst1 = list(d1.values())
            lst2 = list(d2.values())

            lst3 = list(d1.keys())
            lst4 = list(d2.keys())

            if sorted(lst1) == sorted(lst2) and sorted(lst3) == sorted(lst4):
                return True
            else:
                return False
