class Solution:
    def trap(self, height: list[int]) -> int:
        overall_max = 0
        l = 0
        if len(height) <= 2:
            return 0

        while height and len(height) > 2 and height[l + 1] > height[l]:
            height.pop(l)
        while height and len(height) > 2 and height[-2] > height[-1]:
            height.pop()

        if len(height) == 3:
            return min(height[0], height[-1]) - height[1]

        current_max = height[0]
        current_max_index = 0
        overall_max = height[0]
        ans = 0
        i = 1

        while i < (len(height)):
            # Move forward as long as current_val < overall_max
            if height[i] < overall_max:
                i += 1
                # If we reach the end of the table and we did not encounter a value higher than overall_max, we go back until overall_max
                if i == len(height):
                    # we are at the end of the table, let us count back until overall max
                    reversed = height[current_max_index:]
                    reversed.reverse()
                    ans += self.trap(reversed)

            else:
                overall_max = height[i]

                for val in height[current_max_index:i]:
                    ans += current_max - val

                current_max_index = i
                current_max = overall_max
                i += 1

        if ans < 0:
            return 0
        return ans
