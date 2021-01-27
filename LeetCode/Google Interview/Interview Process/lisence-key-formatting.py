'''
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Armando Banuelos 1/27/2021
'''

'''
    Solution: For this, I first go through the array once to extract all characters. And insert them in reverse
    order in an array. Next from that reversed array, I make groups of K size and add them to an all_groups list.
    Lastly I query from all_groups and concatenate together to make the required output. 

    Time Complexity: O(n) - each time we only iterate through the n characters once to get what chars are available
    Space Complexity: O(n^2) - because of all_chars along with all_groups
'''
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        #First go through string S to get all chars available starting from the end
        all_chars = []
        for i in range(len(S)-1, -1, -1):
            if S[i] != "-":
                all_chars.append(S[i])

        #Next we form groups of K from all_chars
        all_groups=[]
        curr_group_size = 0
        curr_string = ""
        for c in all_chars:
            if curr_group_size == K:
                all_groups.append(curr_string[::-1])
                curr_group_size = 0
                curr_string = ""
            curr_string += c.upper()
            curr_group_size += 1
        
        all_groups.append(curr_string[::-1])
        
        result = ""
        #We retrieve all groups and append the dash from reverse order of all_groups
        for i in range(len(all_groups)-1, -1, -1):
            if i > 0:
                result += all_groups[i] + "-"
            else:
                result += all_groups[i]
       
        return result