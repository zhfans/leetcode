class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate, count = 0, 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1

        return candidate


# https://leetcode.com/problems/majority-element/description/
