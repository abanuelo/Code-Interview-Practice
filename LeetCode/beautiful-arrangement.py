'''
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
- 1. perm[i] is divisible by i.
- 2. i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

Armando Banuelos: 1/25/2021
'''

'''
Naive solution:
---------------------------------------------------------------------------------------------------
Create all possible permutations of numbers from input n. Iterate through all permutations to see if
either test case 1. or 2. above apply.

Time Complexity: O(n!) - since we are finding all types of permutations
Space Complexity: O(n!) - since we are storing generator object in all_perms it is O(n!)
'''
class Solution:
    def countArrangement(self, n: int) -> int:
        #Beautiful Arrangement Count
        b_count = 0

        #Find first permutation (ie n = 3 : a = [1, 2, 3])
        a = [i for i in range(1, n+1)]
        
        all_perms = self.find_all_perms(a)
        for perm in all_perms:
            isBeautiful = True
            for i in range(0, len(perm)):
                if (perm[i] % (i+1) != 0) and ((i+1) % perm[i] != 0):
                    isBeautiful = False
                if isBeautiful == False:
                    break
            if isBeautiful == True:
                b_count += 1
        return b_count
                
    
    def find_all_perms(self, a):
        if len(a) <= 1:
            yield a
        else:
            for perm in self.find_all_perms(a[1:]):
                for i in range(len(a)):
                    yield perm[:i] + a[0:1] + perm[i:]