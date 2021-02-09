'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n))

Armando Banuelos 2/9/2021
'''

'''
    Solution: The way this solution works is we add a new merged array nums1 and num2 and then we sort it.
    Then we check the length of the array, if its even then we return the average of the two middle values
    and if the length is odd we return the middle value

    Time Complexity: O(log(m+n)) where m is items in nums1 and n is items in nums2
    Space Complexity: O(m + n) to store the newly merged array
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged) % 2 == 0:
            first_pos = int((len(merged)-1) / 2.0)
            print(first_pos)
            second_pos = first_pos + 1
            print(second_pos)
            return (merged[first_pos] + merged[second_pos])/2.0
        else:
            return merged[int(len(merged) / 2)]