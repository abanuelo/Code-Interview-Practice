'''
You are given an integer array A. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

Armando Banuelos 1/26/2020
'''

'''
    Naive Solution: following the above rules, we created a case for even and odd jumps and test accordingly
    Issue: TimeOut Error within LeetCode

    Time Complexity: O(n^3) - This is n^3 where n is the size of A since we make a call to find the Indexes
    Space Complexity: O(1) - Only storage is the number of good start indicies
'''
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        num_good_start_indicies = 0
        for i in range(len(A)):
            num_jumps = 1
            curr_index = i
            can_jump = True
            while (can_jump):
                #We have reached the end, making this index i a good start index
                if curr_index == len(A)-1:
                    num_good_start_indicies += 1 
                    break
                    
                #Jumps for even cases (jump 2, 4, 6...) 
                if num_jumps % 2 == 0:
                    A_i = A[curr_index]
                    A_possible_jumps = [x for x in A[curr_index+1:] if x <= A_i]
                    if len(A_possible_jumps) > 1:
                        A_j = max(A_possible_jumps)
                        curr_index = self.findIndex(curr_index, A, A_j)
                        num_jumps += 1
                    elif len(A_possible_jumps) == 1:
                        A_j = A_possible_jumps[0]
                        curr_index = self.findIndex(curr_index, A, A_j)
                        num_jumps += 1
                    else: 
                        can_jump = False
                    
                #Jumps for odd cases (jump 1, 3, 5, ...)
                else:
                    A_i = A[curr_index]
                    A_possible_jumps = [x for x in A[curr_index+1:] if x >= A_i]
                    if len(A_possible_jumps) > 1:
                        A_j = min(A_possible_jumps)
                        curr_index = self.findIndex(curr_index, A, A_j)
                        num_jumps += 1
                    elif len(A_possible_jumps) == 1:
                        A_j = A_possible_jumps[0]
                        curr_index = self.findIndex(curr_index, A, A_j)
                        num_jumps += 1
                    else:
                        can_jump = False
        return num_good_start_indicies
        
    def findIndex(self, ind, A, A_j):
        index = 0
        for i in range(ind+1, len(A)):
            if A[i] == A_j:
                index = i
                break
        return index

'''
    Better Solution: In this case we store a dictionary mapping values to their respective indicies for easy retrieval
    Issue: TimeOut Error within LeetCode

    Time Complexity: O(n^2) where n is the size of A
    Space Complexity: O(n) from dictionary
'''
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        num_good_start_indicies = 0
        
        num_to_indicies = {}
        for i,a in enumerate(A):
            if a not in num_to_indicies.keys():
                num_to_indicies[a] = [i]
            else:
                num_to_indicies[a].append(i)
        
        for i in range(len(A)):
            num_jumps = 1
            curr_index = i
            can_jump = True
            while (can_jump):
                #We have reached the end, making this index i a good start index
                if curr_index == len(A)-1:
                    num_good_start_indicies += 1 
                    break
                    
                #Jumps for even cases (jump 2, 4, 6...) 
                if num_jumps % 2 == 0:
                    A_i = A[curr_index]
                    A_possible_jumps = [x for x in A[curr_index+1:] if x <= A_i]
                    if len(A_possible_jumps) > 1:
                        A_j = max(A_possible_jumps)
                        curr_index = self.getIndex(num_to_indicies[A_j], curr_index)
                        num_jumps += 1
                    elif len(A_possible_jumps) == 1:
                        A_j = A_possible_jumps[0]
                        curr_index = self.getIndex(num_to_indicies[A_j], curr_index)
                        num_jumps += 1
                    else: 
                        can_jump = False
                    
                #Jumps for odd cases (jump 1, 3, 5, ...)
                else:
                    A_i = A[curr_index]
                    A_possible_jumps = [x for x in A[curr_index+1:] if x >= A_i]
                    if len(A_possible_jumps) > 1:
                        A_j = min(A_possible_jumps)
                        curr_index = self.getIndex(num_to_indicies[A_j], curr_index)
                        num_jumps += 1
                    elif len(A_possible_jumps) == 1:
                        A_j = A_possible_jumps[0]
                        curr_index = self.getIndex(num_to_indicies[A_j], curr_index)
                        num_jumps += 1
                    else:
                        can_jump = False
                        
        return num_good_start_indicies
    
    def getIndex(self, indexes, curr_index):
        index = 0
        if len(indexes) > 1:
            for p in indexes:
                if p > curr_index:
                    index = p
                    break
        else: 
            index = indexes[0]
        return index
                      

'''
    Better Solution II: I have incorporated caching so that any previous state that needs recomputation can easily access it
    Issue: TimeOut Error within LeetCode

    Time Complexity: O(n^2) where n is the size of A
    Space Complexity: O(n^2) from dictionary and cache
'''
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        num_good_start_indicies = 0
        
        #Store dictionary for easy retreival
        num_to_indicies = {}
        for i,a in enumerate(A):
            if a not in num_to_indicies.keys():
                num_to_indicies[a] = [i]
            else:
                num_to_indicies[a].append(i)
        
        #Cache needed for already computed indicies and their decisive factors
        cache_even = {}
        cache_odd = {}
        
        for i in range(len(A)):
            num_jumps = 1
            curr_index = i
            can_jump = True
            while (can_jump):
                #We have reached the end, making this index i a good start index
                if curr_index == len(A)-1:
                    num_good_start_indicies += 1 
                    break
    
                #Jumps for even cases (jump 2, 4, 6...) 
                if num_jumps % 2 == 0:
                    if curr_index in cache_even.keys():
                        element = cache_even[curr_index]
                        if element[0] == True:
                            curr_index = element[1]
                            num_jumps += 1
                        else:
                            can_jump = False
                    else: 
                        A_i = A[curr_index]
                        A_possible_jumps = [x for x in A[curr_index+1:] if x <= A_i]
                        if len(A_possible_jumps) > 1:
                            A_j = max(A_possible_jumps)
                            prev_index = curr_index
                            curr_index = self.getIndex(num_to_indicies[A_j], curr_index)
                            cache_even[prev_index] = [True, curr_index]
                            num_jumps += 1
                        elif len(A_possible_jumps) == 1:
                            A_j = A_possible_jumps[0]
                            prev_index = curr_index
                            curr_index = self.getIndex(num_to_indicies[A_j], curr_index)
                            cache_even[prev_index] = [True, curr_index]
                            num_jumps += 1
                        else: 
                            can_jump = False
                            cache_even[curr_index] = [False, None]
                        
                #Jumps for odd cases (jump 1, 3, 5, ...)
                else:
                    if curr_index in cache_odd.keys():
                        element = cache_odd[curr_index]
                        if element[0] == True:
                            curr_index = element[1]
                            num_jumps += 1
                        else:
                            can_jump = False
                    else: 
                        A_i = A[curr_index]
                        A_possible_jumps = [x for x in A[curr_index+1:] if x >= A_i]
                        if len(A_possible_jumps) > 1:
                            A_j = min(A_possible_jumps)
                            prev_index = curr_index
                            curr_index = self.getIndex(num_to_indicies[A_j], curr_index)
                            cache_odd[prev_index] = [True, curr_index]
                            num_jumps += 1
                        elif len(A_possible_jumps) == 1:
                            A_j = A_possible_jumps[0]
                            prev_index = curr_index
                            curr_index = self.getIndex(num_to_indicies[A_j], curr_index)
                            cache_odd[prev_index] = [True, curr_index]
                            num_jumps += 1
                        else:
                            can_jump = False
                            cache_odd[curr_index] = [False, None]
                        
        return num_good_start_indicies
    
    def getIndex(self, indexes, curr_index):
        index = 0
        if len(indexes) > 1:
            for p in indexes:
                if p > curr_index:
                    index = p
                    break
        else: 
            index = indexes[0]
        return index


'''
    Let me start off by saying that this solution is absolutely dazling. And I am going to write a good description so I don't forget it

    The idea is if you know that from an odd jump you jump to a state and in that state from an even jump you can get to the end, then you have
    a good start path.
    1. We sort all next odd paths from least to greatest since if you are on odd, the next step you should go to is the largest minmum number
        From 1, we get an oddnext array that looks like this [2,3,3,4,None]. What this is saying is taking the normal orientation of input let's say
        [10 13 12 14 15] for instance, it tells you the index of which state odd should go to. Like oddnext[0] = 2 so its telling us that from 10
        if we take an odd step we go to 12 which is index 2. It does this via a monotonic stack, ensuring that we always hit an index greater (ie the i > stack[-1]
        in the make function)
    2. On a similar note, we do the exact same thing for evennext but this case we know that if we are on an even jump, we only want to go to numbers
        strictly smaller than or equal to us. So we sort the indexes of our path by negative A[i] to get the same desired effect. And the output will look like
        [None, 2, None , None, None] which is saying, in the event we land on index 1 which is 13 (ie [10, 13, 12, 14, 15]) the only possible next position
        is to index 2 which is 12, This makes sense! How beautiful my God.
    3. The last part creates two arrays odd and even of size N with True and false values. The last state will always be True because you know that's our goal!
        So then we do 2 different checks: we start off first with odds because jump 1 -> 2. We check if that value if its possible to jump (ie not None), whatever
        index that position is we check in our even to see if we can set odd at that index to T or F in the event that it reaches the end. Same thing for evens. We
        We check if evennext has a potential place to go to. If it does we mark our even T/F table with the value in our odd T/F table at the result index.

    Like I repeat again and again. Brilliant. Absolutely brilliant! 

    Time Complexity: O(nlogn)
    Space Complexity: O(n)

'''
class Solution(object):
    def oddEvenJumps(self, A):
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key = lambda i: A[i])
        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True

        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)