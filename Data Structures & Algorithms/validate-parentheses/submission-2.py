class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] # basically a list 
        CloseToOpen = {"]":"[", "}":"{", ")":"("} # hashmap with the pairings

        for char in s:
            if char in CloseToOpen:
                if stack and stack[-1] == CloseToOpen[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False

        