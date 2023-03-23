class Solution:
    def search(self, nums: list[int], target: int) -> int:
        print(f"target: {target}, nums: {nums}")
        l = 0 # 0
        r = len(nums) - 1 # 2
        middle = 0 # 1
        while l <= r:
            middle = (l + r) // 2
            if target < nums[middle]:
                r = middle - 1
                print(f"l:{l}, r:{r}, middle: {middle}")
            elif target > nums[middle]:
                l = middle + 1
                print(f"l:{l}, r:{r}, middle: {middle}")
            else:
                return middle
        return -1