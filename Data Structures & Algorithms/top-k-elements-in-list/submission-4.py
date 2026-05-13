class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # return the k most freq elements
        # order can be anything

        # we will use BUCKET SORT

        # a hashmap that counts the occurrence of each element
        count = {} # number : frequency

        freq = [] # an array which has the same number of arrays 
        #within it, as the length of the input array 
    
        for i in range(len(nums)+1):
            freq.append([])

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for number,count in count.items():
            freq[count].append(number) # number occurs count number of times

        result = [] # stores the final values (the top k elements)
        for i in range(len(freq)-1, 0, -1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result


