# 4. Median of Two Sorted Arrays
class Solution:

    def getMedianSortedArray(self,nums: list[int]) -> float:
        return nums[len(nums) // 2] if len(nums) % 2 == 1 else (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if not nums1:
            return self.getMedianSortedArray(nums2)
        if not nums2:
            return self.getMedianSortedArray(nums1)
        
        # Let us assume nums1 is always smaller than nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Compute total length and its half
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2

        # Use binary search on the small array to compute the left partition 
        # and the large array to compute the right partition

        # Loop until a median is found
        # Compute the median for the small array
        l, r = 0, len(nums1) - 1
        while True:
            median_s = (l + r) // 2 # median of the small array
            median_l = half_len - median_s - 2 # median of the large array

            # Compare between the right/left most value of the left/right partition of nums1
            # and the left/right most value of the right/left partition of nums2
            left_nums1 = nums1[median_s] if median_s >= 0 else float("-inf")
            right_nums1 = nums1[median_s + 1] if (median_s + 1) < len(nums1) else float("inf")

            left_nums2 = nums2[median_l] if median_l >= 0 else float("-inf")
            right_nums2 = nums2[median_l + 1] if (median_l + 1) < len(nums2) else float("inf")

            # Check if the partitions are built correctly
            if left_nums1 <= right_nums2 and left_nums2 <= right_nums1:
                # Two possitibilities total_len could be odd or even
                if total_len % 2 == 1:
                    return min(right_nums1, right_nums2)
                else:
                    return (max(left_nums1,left_nums2) + min(right_nums1,right_nums2)) / 2.0
            elif left_nums1 > right_nums2: # reduce the left partition of nums1
                r = median_s - 1 
            else: 
                l = median_s + 1

                    





        
        



    
nums1 = []
nums2 = [3,4]

print(f" --- ANSWER: {Solution().findMedianSortedArrays(nums1,nums2)}")