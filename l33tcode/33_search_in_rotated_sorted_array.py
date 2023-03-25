# 33. Search in Rotated Sorted
class Solution:

    def searchMinIdx(self,nums:list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        idx_min = 0
        
        while l <= r :
            mid = (l + r) // 2
            # Look to the right side
            if nums[mid] >= nums[l]:
                l = mid + 1
                if l < n and nums[l] < nums[mid]:
                    return l
            # Look to the left side
            else:
                r = mid - 1
        return idx_min if min(nums[idx_min], nums[mid]) == nums[idx_min] else mid
    def searchBin(self, nums: list[int], target: int) -> int:
        print(f"target: {target}, nums: {nums}")
        l = 0 # 0
        r = len(nums) - 1 # 2
        middle = 0 # 1
        while l <= r:
            middle = (l + r) // 2
            if target < nums[middle]:
                r = middle - 1
            elif target > nums[middle]:
                l = middle + 1
            else:
                return middle
        return -1
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        ans = -1
        
        offset = 0
        # print(f"l:{l}, r:{r}, middle:{m}")
        # # Find the idx of min(nums)
        if nums[0] > nums[-1]:
            idx_min = self.searchMinIdx(nums)
            print(f"idx_min:{idx_min}")
            if target  == nums[idx_min]: return idx_min

            if idx_min != 0:
                if target < nums[0]: # target must be on the right side
                    print(f"Searching {target} in {nums[idx_min+1:]}...")
                    offset = self.searchBin(nums[idx_min+1:],target)
                    if offset != -1:
                        ans = idx_min + offset + 1
                elif target > nums[0]: # target must be on the left side
                    print(f"Searching {target} in {nums[:idx_min]}...")
                    offset = self.searchBin(nums[:idx_min],target)
                    if offset != -1:
                        ans = offset
                elif target == nums[0]: return 0

                return ans 
        else:
            return self.searchBin(nums,target)


# nums = [4,5,6,7,0,1,2]
# nums = [1,3]
# ret = Solution().search(nums,3)
# print(f" --- ANSWER: {ret} --- ")