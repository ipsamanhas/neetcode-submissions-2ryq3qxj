class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # a sliding window problem
        # asks us to find the length of the longest sub-string
        # but the characters cannot be repeated
        # the strings need to be consecutive/adjacent

        chars = set() # a set doesnt have duplicates
        left = 0
        length = 0 # stores the final length

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            length = max(length, right-left+1)

        return length

        