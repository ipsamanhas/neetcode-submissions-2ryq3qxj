class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the list first
        # let i iterate through the whole array
        # assign two pointers - left and right for each value of i such that nums[i] + nums[left] + nums[right] = 0
        # essentially just use a 2 pointer (2 sum) stratergy
        # time complexity is O(n^2)

        nums.sort()
        result = [] # will store all valid triplets

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue #we dont wanna reuse the same value as before, so we just continue (we dont want duplicates)

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else: # if the sum = 0, basically means that we found a triplet
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)
                    left += 1
                    right -= 1
                    
                    # skipping duplicates but for the pointers
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            

        return result




        