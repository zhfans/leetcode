class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


# https://leetcode.com/problems/contains-duplicate/description/
