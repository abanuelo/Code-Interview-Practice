'''
Given a string s, find the length of the longest substring without repeating characters.

Armando 1.19.2021
'''

'''
    For this solution I would iterate through all chars of the string. Build up a non-repeat array and calculate
    to see at which index i that array would be largest. If that longest is greater than the remainder of the array
    I stop early.

    Time Complexity: O(n^2)
    Space Complexity: O(n) to store the set_nonrepeat
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        longest_subseq_len = 0 
        
        for i in range(len(s)):
            #If the length is just greater than whats left to scan through string s, leave early
            if longest_subseq_len > len(s[i: ]):
                break
                
            set_nonrepeat = []
            set_nonrepeat.append(s[i])
            next_i = i + 1
        
            #continue moving forward in the string until we find a repeated char or we reach end
            if next_i <= len(s)-1:
                while s[next_i] not in set_nonrepeat:
                    set_nonrepeat.append(s[next_i])
                    next_i += 1
                    if next_i > len(s)-1:
                        break
                
                #Compare if we retrieved longest_subseq_len
                if len(set_nonrepeat) > longest_subseq_len:
                    longest_subseq_len = len(set_nonrepeat)
                
        
        return longest_subseq_len