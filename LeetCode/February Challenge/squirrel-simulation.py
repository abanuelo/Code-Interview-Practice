'''
There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
Example 1:
Input: 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:

Armando 2/4/2021
'''

'''
    This solution needs reworking. Can we order nuts in a certain way to speed up retrieval?

    Time Complexity: O(n)
    Space Complexity: O(1)
'''
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        #Idea is to maybe use dijkstra's algorithm to find the shortest path acorn
        min_nut_dist = float('inf')
        min_nut_path = None
        
        #First is to find the closest nut to the squirrel and go to it

        for n in nuts:
            if n[0] <= height-1 and n[1] <= width-1:
                total_distance = abs(squirrel[0] - n[0]) + abs(squirrel[1] - n[1])
                #print("total distance for n: ", n, total_distance)
                if total_distance < min_nut_dist:
                    min_nut_dist = total_distance
                    min_nut_path = n
        
        nuts.remove(min_nut_path)
        #print(min_nut_dist)
        #print(min_nut_path)
        #Then we go from that nut position to the tree and add it to min_nut_dist
        min_nut_dist += abs(min_nut_path[0] - tree[0]) + abs(min_nut_path[1] - tree[1])
        
        #Now it doesn't really matter how we go about the rest of the nuts so let's just find
        #their distances and append it to min_nut_dist cause we can only carry one nut at a time
        for n in nuts:
            if n[0] <= height-1 and n[1] <= width-1:
                min_nut_dist += (abs(tree[0] - n[0]) + abs(tree[1] - n[1])) + (abs(n[0] - tree[0]) + abs(n[1] - tree[1])) # we multiply by 2 to get distance to and from nut
        return min_nut_dist