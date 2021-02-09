'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Armando Banuelos 2/9/2021
'''


'''
    For this solution we just traverse a Binary Search Tree and modify the count nonlocal variable 
    after traversing the right side of the tree.

    Time Complexity: O(n) since we traverse each node once
    Space Complexity: O(1) - just count is stored
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        def traverseTree(root):
            nonlocal count
            if root == None:
                return
        
            traverseTree(root.right)
            root.val += count
            count = root.val
            traverseTree(root.left)
            
            return
        
        count = 0
        traverseTree(root)
        return root
        