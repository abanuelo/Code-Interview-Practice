'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Armando Banuelos 2/4/2021
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
'''

'''
    This attempt at the problem and was submitted successfully. First we will go through and store the count of the values
    in the array. For instance in the above example it would make: {1:1, 2:3, 3:2, 5:1, 7:1}. Then we iterate
    through the array again and just find the n+1 value from the current value if present and add the dictionary values
    at those keys.

    Time Complexity O(n) where n is the size of nums
    Space Complexity: O(n) where n is the size of nums stored in the dictionary
'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #Base case where nums is of length 1
        if len(nums) == 1:
            return 0
        
        max_harmonious = 0
        map_count = {}
        
        #Constuct a dictionary mapping values to count in nums
        for n in nums:
            if n not in map_count.keys():
                map_count[n] = 1
            else:
                map_count[n] += 1
        
        #iterate through array and find count from map_count values 
        cache = []
        for n in nums:
            if n not in cache:
                cache.append(n)
                if n+1 in map_count.keys():
                    result = map_count[n] + map_count[n+1]
                    if result > max_harmonious:
                        max_harmonious = result
        
        return max_harmonious