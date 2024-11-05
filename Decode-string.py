# Problem: Decode String
# Difficulty: Medium
# Runtime: 3 ms (Beats 95% of LeetCode users)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s: 
            if i != ']': 
                stack.append(i)
            else: 
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
            
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * temp)

        return ''.join(stack)
