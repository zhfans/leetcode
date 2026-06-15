class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, k = 0, 0

        while k < len(nums) - i:
            if nums[k] != val:
                k += 1
                continue

            if nums[-i - 1] == val:
                i += 1
                continue

            nums[k] = nums[-i - 1]
            nums[-i - 1] = val

        return k


# https://leetcode.com/problems/remove-element/description/
