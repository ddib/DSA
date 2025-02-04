from collections import deque
def rotting_oranges(grid):
    """
    Problem:
    Given a grid of numbers where each cell can have one of three values:
    0: Represents an empty cell.
    1: Represents a fresh orange.
    2: Represents a rotten orange.
    Every minute, any fresh orange that shares a side with a rotten orange also becomes rotten. 
    Return the minimum time after which all the oranges will rot.
    If there exists any orange that will never rot, return -1.
    https://leetcode.com/problems/rotting-oranges/description/

    
    Complexity:
    * Time: O(n * m), n: number of rows. m: number of columns.
    * Space: O(n * m)
    """
    
    n = len(grid)
    m = len(grid[0])
    
    def get_neighbors(i, j):
        output = []
        for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nei_x, nei_y = i + x, j + y
            if 0 <= nei_x < n and 0 <= nei_y < m:
                output.append((nei_x, nei_y))
        return output 
    
    # get the sources O(n x m)
    queue = deque()
    for raw in range(n):
        for col in range(m):
            if grid[raw][col] == 2:
                queue.append((raw, col))
                
    # multisource BFS traversal 
    minutes = 0           
    while queue:
        minutes += 1
        current_level = len(queue)
        for _ in range(current_level):
            i, j = queue.popleft()
            neighbors = get_neighbors(i, j)
            for x, y in neighbors:
                if grid[x][y] == 1:
                    grid[x][y] = 2 # needed for checking left cells
                    queue.append((x, y))
            
    # check for any left cell O(n x m)
    for raw in range(n):
        for col in range(m):
            if grid[raw][col] == 1:
                return -1
                
    return max(0, minutes -1)
