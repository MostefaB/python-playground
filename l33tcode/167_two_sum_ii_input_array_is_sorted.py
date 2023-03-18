class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        if len(numbers) == 2:
            return [1, 2]
        l = (0,)
        r = len(numbers) - 1
        for l, xA in enumerate(numbers):
            lookup = target - xA
            while r > l:
                if lookup > numbers[r]:
                    break
                elif lookup == numbers[r]:
                    return [l + 1, r + 1]
                elif lookup < numbers[r]:
                    r -= 1
