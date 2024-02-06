# Date: 2/6/2024
# Basic Solution (Runtime: 65ms)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ""
        if len(word1) > len(word2):
            for i in range(len(word2)):
                newWord = newWord + word1[i] + word2[i]
            return newWord + word1[len(word2):]
        elif len(word2) > len(word1):
            for j in range(len(word1)):
                newWord = newWord + word1[j] + word2[j]
            return newWord + word2[len(word1):]
        else:
            for k in range(len(word1)):
                newWord = newWord + word1[k] + word2[k]
            return newWord


# Efficient Solution (Runtime: 32ms)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0 
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i = i + 1
            j = j + 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
