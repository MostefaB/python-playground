# 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        max_sub_arr = nums[0]
        running_sum = 0

        for n in nums:
            if running_sum < 0:
                running_sum = 0
            running_sum = running_sum + n
            max_sub_arr = max(max_sub_arr,running_sum)
  
        return max_sub_arr



# nums = [-2,1,-3,4,-1,2,1,-5,4]
# ret = Solution().maxSubArray(nums)
# print(f" --- ANSWER: {ret} --- ")