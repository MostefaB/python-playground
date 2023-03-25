# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2: return min(nums[0],nums[1]) if n == 2 else nums[0]

        l = 0
        r = n - 1
        idx_min = 0

        while l <= r :
            mid = (l + r) // 2
            print(f"l:{l}, r:{r}, mid:{mid}")
            if nums[mid] >= nums[l]:
                l = mid + 1
                if l < n and nums[l] < nums[mid]:
                    return nums[l]
            else:
                r = mid - 1
        return min(nums[idx_min], nums[mid])
         

# nums = [2,3,4,5,1]
# ret = Solution().findMin(nums)
# print(f" --- ANSWER: {ret} --- ")
