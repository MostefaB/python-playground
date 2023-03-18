class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]
        output = [len(nums)]
        output[0] = 1
        count = {}
        prefix = 1
        for i in range(0, len(nums) - 1):
            prefix = prefix * nums[i]
            output.append(prefix)

        # print(i)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # print(i)
            output[i] = postfix * output[i]
            postfix = postfix * nums[i]
            # print(f"postfix={postfix}")
            # if i ==0:
            #     output[0] = post

        return output
