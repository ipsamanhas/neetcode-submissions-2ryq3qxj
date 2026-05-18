class Solution:
    def trap(self, height: List[int]) -> int:

        # max amount of rainwater the whole structure can trap
        # each element in the array is the height at that index

        left = 0
        right = len(height)-1
        maxLeft = height[left]
        maxRight = height[right]
        result = 0 # will store the final result (keep adding to it)

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                diff = maxLeft - height[left]
                result += diff
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                diff = maxRight - height[right]
                result += diff

        return result

        