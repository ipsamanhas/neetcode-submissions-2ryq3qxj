class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {} # hashmap to store the count of each distinct element
        left = 0
        length = 0 # stores the longest length of the sub-string

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)

        return length

        