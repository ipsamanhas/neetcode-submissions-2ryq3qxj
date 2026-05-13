# EASY QUESTION ONCE U UNDERSTAND THE METHOD U WANNA USE

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""  # combined string i.e encoded
        
        # this is how I will encode my string
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

        # encoded string will look something like : "4#neet4#code"

    def decode(self, str: str) -> List[str]:
        result = []  # need to return a list at the end
        i = 0  # first index

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1 # keep incrementing j until it reaches the #
            length = int(str[i:j])
            word = str[j + 1 : j + 1 + length]
            result.append(word)
            i = j + 1 + length
        return result