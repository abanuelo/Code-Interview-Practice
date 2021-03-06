'''
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Armando Banuelos 1/27/2021
'''

'''
    Naive Solution: We will iterate over the tree and try to locate the biggest sequence of two types of fruits;
    The fruit types will hold the two different types of fruit and we will iterate past the i+1 index to ensure 
    that another fruit type or that same fruit type at the ith index exists and increment our fruit_count accordingly.
    Problem: Timeout Error

    Time Complexity: O(n^2)
    Space Complexity: O(1)
'''
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        total_fruit = 0
        fruit_types = []
        for i in range(len(tree)):
            fruit_count = 1
            fruit_types.append(tree[i])
            for j in range(i+1, len(tree)):
                if len(fruit_types) == 1 and tree[j] in fruit_types:
                    fruit_count += 1
                elif len(fruit_types) == 1 and tree[j] not in fruit_types:
                    fruit_types.append(tree[j])
                    fruit_count += 1
                else:
                    if tree[j] in fruit_types:
                        fruit_count += 1
                    else:
                        break
                    
            fruit_types = []
            if fruit_count > total_fruit:
                total_fruit = fruit_count
        
        return total_fruit

'''
    Note that this solution was devised on 1.29.2021
    Solution: To make minor modifications to the attempt above, essentially, what we needed to do was
    to ensure that we start from the next index of the second type instead of using for i in range to iterate
    through all elements

    Time-Complexity: O(n) where n is the size of tree
    Space-Complexity: O(1) using minimal space to only store index starts (i and next_start)
'''
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        total_fruit = 0
        fruit_types = []
        i = 0
        next_start = 0
        
        if len(tree) < 3:
            return len(tree)
        
        while next_start < len(tree)-1:
            fruit_count = 1
            fruit_types.append(tree[i])
            for j in range(i+1, len(tree)):
                if len(fruit_types) == 1 and tree[j] in fruit_types:
                    fruit_count += 1
                elif len(fruit_types) == 1 and tree[j] not in fruit_types:
                    fruit_types.append(tree[j])
                    fruit_count += 1
                    next_start = j
                else:
                    if tree[j] in fruit_types:
                        fruit_count += 1
                    else:
                        break
                if (j == len(tree)-1):
                    next_start = j
            
            fruit_types = []
            if fruit_count > total_fruit:
                total_fruit = fruit_count
            i = next_start
        return total_fruit
                