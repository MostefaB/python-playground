class Solution:
    # @staticmethod
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
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # BruteForce loop through matrix with two indices O(n.m)
        # Merge + Binary Search: O(m)+O(log(n.m)) ==? O(m)
        # What if we applied a two dimension Binary Search for O(log(n.m))

        print(matrix, target)
        n = len(matrix) # nb rows
        m = len(matrix[0]) # nb cols

        up, down = 0, n - 1
        l, r = 0, m - 1

        while up <= down:

            mid_height = (down + up) // 2 # 1
            if target < matrix[mid_height][0]:
                down = mid_height - 1 #
            elif target > matrix[mid_height][m-1]:
                up = mid_height + 1
            elif matrix[mid_height][0] <= target <= matrix[mid_height][m-1]:
                # Look for target in the mid_height-th row using Binary Search
                row = matrix[mid_height]
                ret_row = self.search(row, target)
                return ret_row != -1
        return False

# ret = Solution().searchMatrix(matrix,11)