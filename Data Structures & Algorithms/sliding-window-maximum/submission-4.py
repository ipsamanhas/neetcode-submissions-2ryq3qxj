class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # the window is of size k
        # the window keeps sliding through the array till the end
        # at each window it returns the max element
        
        # BRUTE FORCE APPROACH
        # results = []

        # for right in range(len(nums) - k + 1):
        #     window = nums[right:right+k]
        #     results.append(max(window))

        # return results

# ACTUAL SOLUTION

        result = [] # final ans
        left = right = 0
        q = collections.deque() # made a queue -> stores indices

        for right in range(len(nums)):
            # pop smaller elements from the queue
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right) # append the indices only (we can map them to the corresponding element in the array)

            # remove left value from the window
            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                result.append(nums[q[0]])
                left += 1
            right += 1
        
        return result



        