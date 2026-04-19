from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list) #sorted letters:list of words
        values = []

        # we cannot have a list as a key, but tuples can be keys
        for s in strs:
            s_sorted = tuple(sorted(s)) #this will sort each word
            anagrams[s_sorted].append(s) #its a key:value pair, so i'm just appending a value to each key
        
        # anagrams.values() returns lists with anagrams
        for value in anagrams.values():
            values.append(value)

        return values        

        #time complexity - O(n * klog(k))
        #memory complexity - O(n*k)