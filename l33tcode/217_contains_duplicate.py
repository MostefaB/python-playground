class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for n in nums:
            if not n in my_set:
                my_set.add(n)

            else:
                return True

        return False
