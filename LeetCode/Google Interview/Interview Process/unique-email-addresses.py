'''
Every email consists of a local name and a domain name, separated by the @ sign.
For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
Besides lowercase letters, these emails may contain '.'s or '+'s.
If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)
If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

Armando Banuelos 1/26/2020
'''

'''
    For this solution, we will iterate through each email in emails and separate domain and local names. We then clean the local 
    names according to the preable of the problem such that everything after '+' gets ignored and all '.' when removed create
    equivalent emails. Then we add our cleaned email to a list and increment the count of total unique email addresses to send

    Time Complexity: O(n) where n is the size of emails
    Space Complexity: O(n) where n is the size of emails (we store cleaned emails in the all_emails array)
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        all_emails = []
        total_emails = 0
        for i,email in enumerate(emails):
            #For every email let's first separate domain and local names
            email_split = email.split('@')
            unclean_local_name = email_split[0]
            domain_name = email_split[1]
        
            #Step One: For local name, split at plus and retain first half of split
            cleaner_local_name = unclean_local_name.split('+')[0]
    
            #Step Two: For local name, replace all periods with empty characters
            local_name = cleaner_local_name.replace('.','')
            
            new_email = local_name + "@" + domain_name
 
            if new_email not in all_emails:
                all_emails.append(new_email)
                total_emails += 1
        return total_emails


            
            
        