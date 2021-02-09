'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.

Armando Banuelos 2/9/2021
'''

'''
    The first way to approach this problem is to simply do DFS on all island nodes within the grid
    and to store their shape by takking their existing coordinates and bringing it to their (0,0) origin
    equivalent that way we can easily compare shapes.

    Time Complexity: O(M^2 N^2) where M is the row length and N is the column length and its squared here
                    because we are also itersating through unique_islands
    Space Complexiy: O(M N)
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def current_island_is_unique():
            for other_island in unique_islands:
                if len(other_island) != len(current_island):
                    continue
                for c1, c2 in zip(current_island, other_island):
                    if c1 != c2:
                        break
                else:
                    return False
            return True
        
        def dfs(row, col):
            #If this row is out of the bounds of our grid
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            #If its in our seen or if its a body of water (0)
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            current_island.append((row-row_origin, col-col_origin))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        #First approach is to apply DFS to all islands and compare the unqiue stored coordinates
        seen = set()
        unique_islands = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = []
                row_origin = row
                col_origin = col
                dfs(row, col)
                #if our current_island is blank or if its not unique we leave
                if not current_island or not current_island_is_unique():
                    continue
                unique_islands.append(current_island)
        return len(unique_islands)
        
'''
    Seeing that the squared from the previous approach was as a result of storing coorindates in a list
    we can use a hash function to store their value and query it in real time using python's frozenset
    command

    Time Complexity: O(mn)
    Space Complexity: O(mn)
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            #If this row is out of the bounds of our grid
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            #If its in our seen or if its a body of water (0)
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            current_island.add((row-row_origin, col-col_origin))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        #First approach is to apply DFS to all islands and compare the unqiue stored coordinates
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)
                #if our current_island is blank or if its not unique we leave
                if current_island:
                    unique_islands.add(frozenset(current_island))
        return len(unique_islands)