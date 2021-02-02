'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

Armando 2/2/2021
'''

'''
My approach was to adopt recursion in order to traverse the tree. We build a current path from the node.val
and the left and right nodes to see if that generates the max sum, if so we return that as max sum. For the recursion
we take the max_node of left and right and the current node value to traverse through the tree's maximum path:

Time Complexity: O(n)
Space Complexity: O(1)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def recursion(node):
            nonlocal max_sum #makes it a global variable
            if not node:
                return 0
            left_gain = max(recursion(node.left), 0)
            right_gain = max(recursion(node.right), 0)
            
            new_path = node.val + left_gain + right_gain
            
            max_sum = max(max_sum, new_path)
            return node.val + max(left_gain, right_gain)
        
        
        #store max sum path
        max_sum = float('-inf')
        recursion(root)
        return max_sum
        
