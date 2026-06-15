class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[last]:
                last += 1
                nums[last] = nums[i]

        return last + 1


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
