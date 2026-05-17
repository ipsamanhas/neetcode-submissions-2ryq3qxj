class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # width = right_index - left_index
        # height = min(heights[right_index], heights[left_index])
        # two-pointer problem

        result = 0 #stores the final result

        left = 0
        right = len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            result = max(area, result) 

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -=1 
            else:
                # we can do either
                right -= 1

        return result