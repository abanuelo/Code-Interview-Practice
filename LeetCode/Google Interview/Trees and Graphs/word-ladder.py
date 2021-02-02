class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        def findCount(w, l, c):
            nonlocal min_changes
            
            if w == endWord:
                return c
            if len(l) == 0:
                return 0
            
            for i in range(len(l)):
                if self.isOneLetterDifferent(w, l[i]):
                    c += 1
                    count = findCount(l[i], wordList.pop(i), c)
                    if count < min_changes:
                        min_changes = count
                        
            return min_changes
                    
        
        #If end not present, not possible
        if endWord not in wordList:
            return 0   
        
        min_changes = float('inf')
        findCount(beginWord, wordList, 0)
        return min_changes
                 
    def isOneLetterDifferent(self, w1, w2):
        print(w1, w2)
        res = False
        char_diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                char_diff += 1
        if char_diff == 1:
            res = True
        return res
                
            
            
            
        