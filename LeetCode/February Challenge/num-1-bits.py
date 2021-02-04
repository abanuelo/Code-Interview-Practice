'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above, the input represents the signed integer. -3.
Follow up: If this function is called many times, how would you optimize it?

Armando Banuelos - 2/4/2021
'''

'''
    Solution: So this involves bitwise operators. We will right-shift bits and AND the result with 1 to see if
    one is present.

    Time Complexity: O(n) where n are the 32 bits
    Space Complexity: O(1)
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        #bitwise shift operators for unsigned integers
        count = 0
        complement = 1
        while n > 0:
            res = complement & n
            count += res
            n = n >> 1
        return count