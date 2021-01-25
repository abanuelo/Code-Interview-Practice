'''
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Armando Banuelos 1/25/2021
'''

'''
This solution is fast and will check the two strings covering the insert, delete, and exchange cases accordingly.
1. If both strings are the same, there is no way to edit s to get t
2. If the length of t is one greater than s, it can be an insertion. So we keep an ins_count variable to ensure that we have
    only one insert total
3. If the length of t is one less than s, it can be a deletion. So we keep an del_count variable to ensure that we have only
    one deletion
4. If the length of s and t are the same, then there may exist an exchange. To test the change we keep a exchange_count variable
    to ensure that only one character has been exchanged
'''
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        #If both strings are the same
        if s == t:
            return False
        
        #There was an insertion
        if len(s) == len(t)-1:
            ins_count = 0
            j = 0
            for i in range(len(t)):
                #In the event the insertion was at the end of the string, it will be True (ie s: cat and t: catb)
                if (j == len(t)-1):
                    return True
                
                if s[j] == t[i]:
                    j += 1
                elif s[j] != t[i]:
                    ins_count += 1
                
                if ins_count > 1:
                    return False
            return True
        
        
        #There was a deletion
        elif len(s) == len(t)+1:
            del_count = 0
            j = 0
            for i in range(len(s)):
                #In the event the deletion was at the end of the string, it will be True (ie s: cat and t: ca)
                if (j == len(s)-1):
                    return True
                if t[j] == s[i]:
                    j +=1
                elif t[j] != s[i]:
                    del_count += 1
                if del_count > 1:
                    return False
            return True
        
        #There was an exchange
        elif len(s) == len(t):
            exchange_count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    exchange_count += 1
                if exchange_count > 1:
                    return False
            return True
        
        else:
            return False