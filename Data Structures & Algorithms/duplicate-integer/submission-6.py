class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # i can use a for loop to go thru the array and add each element of that array to a new one, then i can compare if an element is present in the array alr

        result = set()

        for num in nums:
            if num not in result:
                result.add(num)
            else:
                return True

        return False        