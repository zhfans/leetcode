class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        if nums[0] == 0:
            return False

        farthest = 0
        destination = n - 1
        for i in range(destination):
            farthest = max(farthest, i + nums[i])
            if farthest >= destination:
                return True
            if farthest == i:
                return False

        return True


# https://leetcode.com/problems/jump-game/description/
