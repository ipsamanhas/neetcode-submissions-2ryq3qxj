class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = "" # a new string that will not stores any spaces or non-alphanum characters

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        
        return cleaned == cleaned[::-1]