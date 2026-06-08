class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        last = 1

        for i in range(2, n):
            num = nums[i]
            if num != nums[last - 1]:
                last += 1
                nums[last] = num

        return last + 1


# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
