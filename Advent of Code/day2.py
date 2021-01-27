#Armando Banuelos 1/27/2021

import os

#Store passwords from passwords-input.txt into here
passwords = []
with open('passwords-input.txt') as f:
    for line in f:
        passwords.append(line.strip())

'''
    PART 1:
    ------------------------------------------------------------------------------------
    Given a password policy as follows: 4-10 v: vvvsvvvvvqvvvv, the goal is to check if 'v'
    appears at most 10 times or at least 4 times within the password string

    My approach to this problem is essentially to iterate over all passwords stored from reading
    passwords-input.txt and separate them from their policy and passwords. Iterate through passwords
    and count the number of times that char appears and see if it complies with the password policy
    range

    Time Complexity: O(n^2) where n is the length of password input 
    Space Complexity: O(1)
'''
valid_passwords = 0
for p in passwords:
    #Separate policy and password
    sep = p.split(":")
    policy = sep[0].strip()
    p_word = sep[1].strip()

    #For policy separate char to investigate and range of values char can appear
    sep_pol = policy.split(" ")
    pol_range = sep_pol[0].split("-")
    pol_char = sep_pol[1]

    #Find the number of times char in question appears and store it within c_times
    c_times = 0
    for c in p_word:
        if c == pol_char:
            c_times += 1
    
    #Check if c_times is in accordance with policy range, if so increment valid passwords
    if c_times >= int(pol_range[0]) and c_times <= int(pol_range[1]):
        valid_passwords += 1

print("PART 1 - Total Number of Valid Passwords: ", valid_passwords)


'''
    PART 2:
    ------------------------------------------------------------------------------------
    Given a password policy as follows: 4-10 v: vvvsvvvvvqvvvv, the goal is to check if 'v'
    appears at exactly one only at the 4th position of the password string or the 10th position
    of the password string

    My approach to this problem is essentially to iterate over all passwords stored from reading
    passwords-input.txt and separate them from their policy and passwords. Then I will check the indexes
    of the password as indicated by the policy to ensure that only one of them holds true to have the character
    in question

    Time Complexity: O(n) where n is the length of password input
    Space Complexity: O(1)
'''
valid_passwords = 0

for p in passwords:
    #Separate policy and password
    sep = p.split(":")
    policy = sep[0].strip()
    p_word = sep[1].strip()

    #For policy separate char to investigate and range of values char can appear
    sep_pol = policy.split(" ")
    pol_range = sep_pol[0].split("-")
    pol_char = sep_pol[1]

    #Check the specific indexes of the password string to see if they only contain exactly one of the characters
    if p_word[int(pol_range[0])-1] == pol_char and p_word[int(pol_range[1])-1] != pol_char:
        valid_passwords += 1
    elif p_word[int(pol_range[0])-1] != pol_char and p_word[int(pol_range[1])-1] == pol_char:
        valid_passwords += 1
    else:
        pass
    
print("PART 2 - Total Number of Valid Passwords: ", valid_passwords)







