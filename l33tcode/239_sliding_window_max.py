# 239. Sliding Window Maximum
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # # Bruteforce
        # ans = list() # List to store the maximum values of each window
        # l = 0
        # r = l + (k-1)
        
        # while r < len(nums):
        #     sub = nums[l:r+1]
        #     ans.append(max(sub))
        #     l += 1
        #     r += 1
        # return ans

        # the deque holds the indices
        d = deque()
        # output holds the local max values
        output = list()

        # Loop through the array, i is the "head" of the sliding window
        for i in range(len(nums)):
            # If the deque contains indices and
            # the current element is greater than the right most element in the deque
            # pop it and compare until there are none
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            
            # add the current index the deque - should be in decreasing order
            d.append(i)

            # check if my left most deque index is outside the sliding window
            while d[0] < i - k + 1:
                d.popleft()
            
            # if we are at or past the end of the 1st sliding window, add the nums[left most deque element]
            if i >= k - 1:
                output.append(nums[d[0]])
        return output
