# 84. Largest Rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.
# 
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_surface = 0
        stack = [] # Store index and heights as in (idx,height)
        
        for i, h in enumerate(heights):
            left = i
            while stack and h < stack[-1][1]:
                # fetch the top of the stack that is greater than the current height h
                idx, top_stack_height = stack.pop()
                # Compute surface
                max_surface = max(max_surface, top_stack_height * (i - idx))
                left = idx
            stack.append((left,h))
        
        # Loop through the stack to compute the surface of any remaining heights
        for i, h in stack:
            max_surface = max(max_surface, h * (len(heights) - i))
        
        return max_surface



heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))