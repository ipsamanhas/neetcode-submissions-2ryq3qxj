class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # the element doesn't have to be consecutive in the array

        numSet = set(nums) #it creates a set of the array nums, doesnt have duplicates
        longest = 0  #stores the longest sequence

        for num in numSet:
            if (num-1) not in numSet:
                length = 0
                while (num+length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest

    
        
        