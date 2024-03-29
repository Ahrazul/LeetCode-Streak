# Date completed: 2/9/2024
# Problem name: Kids with greatest number of candies (Easy)
# Runtime: 32ms (Beats 93% of Leetcode users)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maximum = max(candies)
        for i in range(len(candies)):
            var = candies[i] + extraCandies
            if var >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
