# 152. Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # First, we check if the input array is empty. If it is, we return 0.
        if not nums:
            return 0
        # We initialize three variables: max_product, min_product, and result. 
        # We set their initial values to the first element of the input array (nums[0]).
        max_product, min_product, result = nums[0], nums[0], nums[0]

        # We iterate through the input array starting from the second element (index 1) using a for loop.
        for i in range(1,len(nums)):
            # We check if the current element (nums[i]) is negative. 
            # If it is, we swap the values of max_product and min_product. 
            # This is because multiplying a negative number with the current minimum product could result in a maximum product.
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            # We update the max_product by taking the maximum of the current element and the product of the current element and the previous max_product. 
            # This ensures that we're tracking the maximum product subarray ending at the current position.
            max_product = max(nums[i], nums[i] * max_product)
            # Similarly, we update the min_product by taking the minimum of the current element and the product of the current element and the previous min_product. 
            # This ensures that we're tracking the minimum product subarray ending at the current position.
            min_product = min(nums[i], nums[i] * min_product)

            # We update the global result by taking the maximum of the current result and the updated max_product. 
            # This keeps track of the maximum product subarray we've seen so far.
            result = max(max_product, result)
        
        # After the loop, we return the result, which is the largest product of a contiguous subarray
        return result
    
# The time complexity of this solution is O(n) because we iterate through the input array once. 
# The space complexity is O(1) because we only use a constant amount of additional memory to store the local maximum and minimum products and the global result.