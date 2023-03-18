class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxSurface = 0
        l, r = 0, len(height) - 1

        while l < r:
            surface = 0
            minHeight = min(height[l], height[r])
            width = r - l
            surface = minHeight * width
            maxSurface = max(maxSurface, surface)
            # print(f"l:{l}, r:{r}, maxSurface:{maxSurface}, currentSurface:{surface}")
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1

        return maxSurface
