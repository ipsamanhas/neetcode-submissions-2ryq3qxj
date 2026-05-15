# THIS IS ALSO AN AMAZING QUESTION LOWKEY
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

       # just like the 2 sum problem 
       # but we have a 1-indexed array (add +1 to the actual index)
       # arranged in ascending order
       # solution should use O(1) additional space -> no new data structure
       # there will always be a solution 

       left = 0
       right = len(numbers) - 1


       while left < right:
        sum = numbers[left] + numbers[right]

        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        
        # if sum of both the numbers is equal to the target
        else:
            new_indexleft = left + 1
            new_indexright = right + 1
            return [new_indexleft, new_indexright]





    






    #    for num in numbers:
    #     # num + other_num = target
    #     other_num = target - num

    #     # to look for the other_num, we can do a binary search
    #     while left <= right:
    #         mid = left + (right-left) // 2

    #         if numbers[mid] == other_num:
    #             return num, other_num

    #         elif numbers[mid] < other_num:
    #             left = mid + 1
            
    #         else:
    #             right = mid - 1

    #     return num, other_num

