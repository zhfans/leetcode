# https://leetcode.com/problems/valid-anagram/description/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars_reps: list[int] = [0] * 26
        for c in s:
            s_chars_reps[ord(c) - ord("a")] += 1

        for c in t:
            i = ord(c) - ord("a")
            s_chars_reps[i] -= 1
            if s_chars_reps[i] < 0:
                return False

        return True
