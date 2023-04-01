# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait
#  after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        n = len(temps)
        ans = [0] * n
        stack = list()
        # Brute force for each index i loop through i+1 to len(temps)-1 searching for a greater temps[j]
        # add j-i to output if found else 0 - O(n^2) of time complexity
        # for i, t in enumerate(temps):
        #     for j in range(i + 1, len(temps), 1):
        #         if temps[j] > t:
        #             ans[i] = j - i
        #             break
        # return ans
        for i in range(0, n - 1, 1):
            # Check the current and the next temp
            if temps[i] < temps[i + 1]:
                # Update the output if the next day is warmer
                ans[i] = 1
                # Check if the stack is not empty and if next temp is greater than the top of our stack (value at index)
                while stack and temps[stack[-1]] < temps[i + 1]:
                    # Found a warmer temp - let's pop and update the answer at the index that was popped
                    j = stack.pop()
                    ans[j] = i - j + 1
            else:
                # Add the current temp index to the stack
                stack.append(i)
        return ans
