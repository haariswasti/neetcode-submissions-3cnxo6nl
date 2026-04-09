class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = 0
        while l < r:
            x = r - l
            y = x * min(heights[r], heights[l])
            ans = max(ans, y)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans

        