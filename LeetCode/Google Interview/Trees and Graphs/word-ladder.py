'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Armando Banuelos 2/3/2021
'''

'''
This is a valid solution, but it exceeds time limit. Essentially what happens is that we find the count by passing in
the word, find an adjacent word, the recurse by passing in a new wordList with the excluded adjacent list along with a
construction of the path being built. And idea to reduce time limit would be to provide an early termination if our min_changes
is less than the array we are iterating on.

Time Complexity: O(n log(n)) - n for the for loop and log(n) for the findCount feature
Space Complexity: O(n) to store the path which can be at worse size n
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        def findCount(w, l, c):
            nonlocal min_changes
            #print("w, l, and c: ", w, l, c)
            if w == endWord:
                return len(c)
            if len(l) == 0:
                return min_changes
            
            for i in range(0, len(l)):
                #print("l: ", l)
                #print("i: ", i)
                #print("len(l): ", len(l))
                
                if self.isOneLetterDifferent(w, l[i]):
                    #print("original_word: ", w)
                    #print ("new_adjacent_path: ", l[i])
                    adj_word = l[i]
                    c.append(adj_word)
                    new_l = l[:i] + l[i+1:]
                    #print("NEW_L AND L: ", l, new_l)
                    count = findCount(adj_word, new_l, c)
                    if count < min_changes:
                        min_changes = count
                    c.pop(-1)
                        
            return min_changes
                    
        
        #If end not present, not possible
        if endWord not in wordList:
            return 0 
        
        
        path = [beginWord]
  
    
        min_changes = float('inf')
 
        findCount(beginWord, wordList, path)
        
        if min_changes == float('inf'):
            min_changes = 0
        
        return min_changes
                 
    def isOneLetterDifferent(self, w1, w2):
        res = False
        char_diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                char_diff += 1
        if char_diff == 1:
            res = True
        return res

'''
    Solution: Involving breadth first search approach, however it still exceeds the time complexity
    needed to pass the test

    Time Complexity = O(m^2*n) where m is the length of the word, n is the number of words in the list
    Space Complexity = O(m^2*n) because of our dictionary

'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #If end not present, not possible
        if endWord not in wordList:
            return 0 
        
        def findAllNeighbors(w1, l):
            res = []
            for w2 in l:
                if  self.isOneLetterDifferent(w1, w2):
                    res.append(w2)
            return res
                
        
        level = 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        queue = [beginWord]
        while len(queue) != 0:
            #print("queue: ", queue)
            q_size = len(queue)
            level += 1
            for i in range(q_size):
                w = queue.pop(0)
                #print("w: ", w)
                if w == endWord:
                    return level
                neighbors = findAllNeighbors(w, wordList)
                #print("neighbors: ", neighbors)
                for n in neighbors:
                    if n in wordList:
                        wordList.remove(n)
                        queue.append(n)
        
        return 0
                 
    def isOneLetterDifferent(self, w1, w2):
        res = False
        char_diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                char_diff += 1
        if char_diff == 1:
            res = True
        return res
                
'''
    We are now using the idea of a bi-directional Breadth First Search to traverse through paths that have the
    least branching factor to speed up processing. 

    Time Complexity: O(M^2*N) where m is the length of the strings and n is the total wordList length
    Space Complexity: O(M^2*N)
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #If end not present, not possible
        if endWord not in wordList:
            return 0 
        
        def findAllNeighbors(w):
            res = []
            all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            for i in range(len(w)):
                for c in all_letters:
                    neighbor = w[:i] + c + w[i+1:]
                    res.append(neighbor)
            return res
            
        words = set(wordList)
        beginSet = {beginWord}
        endSet = {endWord}
        length = 1
        while(len(beginSet) != 0 and len(endSet) != 0):
            #print(beginSet, endSet)
            if len(beginSet) > len(endSet): 
                tmpSet = beginSet
                beginSet = endSet
                endSet = tmpSet
            newBeginSet = set()
            for w in beginSet:
                neighbors = findAllNeighbors(w)
                #print("neighbors: ", neighbors)
                for n in neighbors:
                    if n in endSet: 
                        return length + 1
                    if n in words: 
                        newBeginSet.add(n)
                        words.remove(n)
            #print("newBeginSet: ", newBeginSet)
            beginSet = newBeginSet
            length += 1
        return 0
            
        