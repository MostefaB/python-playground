class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        # print(nums)
        longest_sequence_so_far = 1
        local_longest = 1
        i = 0

        while i < len(nums) - 1:
            print(f"i = {i}")
            if nums[i] + 1 == nums[i + 1]:
                local_longest += 1
                i += 1
                if i == len(nums) - 1:
                    return max(longest_sequence_so_far, local_longest)
                # print(f"Local longest = {local_longest}, Longest so far = {longest_sequence_so_far}")
            elif nums[i] == nums[i + 1]:
                i += 1
                if i == len(nums) - 1:
                    return max(longest_sequence_so_far, local_longest)

            else:
                longest_sequence_so_far = max(longest_sequence_so_far, local_longest)

                # print(
                #     f"max(longest_sequence_so_far:{longest_sequence_so_far}, local_longest:{local_longest})"
                # )
                local_longest = 1
                i += 1

        return longest_sequence_so_far
