class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x = 0
        l = len(heights) - 1
        max_area = 0
        while x < l:
            area = (l - x) * (min(heights[l],heights[x]))
            if area > max_area:
                max_area = area
            if heights[l] > heights[x]:
                x += 1
            else:
                l -= 1
        return max_area

