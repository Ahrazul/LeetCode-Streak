# Problem: Equal Row and Column Pairs
# Difficulty: Medium
# Runtime: 15 ms (Beats 91% of LeetCode users)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid))]

        d1 = {}

        for row in grid:
            row_tuple = tuple(row) 
            if row_tuple in d1:
                d1[row_tuple] += 1
            else:
                d1[row_tuple] = 1

        count = 0

        for col in transposed:
            col_tuple = tuple(col)  
            if col_tuple in d1:
                count += d1[col_tuple]

        return count

