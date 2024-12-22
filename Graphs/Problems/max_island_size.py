def max_island_size(grid):
    """
    Problem:
    Given a two-dimensional grid of 0s and 1s, find the size of the largest island. If there is no island return 0.
    An island is a group of 1s connected vertically or horizontally.
    https://leetcode.com/problems/max-area-of-island/description/
    
    Complexity:
    * Time: O(nb_rows * nb_cols)
    * Space: O(nb_rows * nb_cols)

    Note: both BFS and DFS traversals solve this problem.
    """
    
    def DFS(i, j):
        nonlocal size
        size += 1
        grid[i][j] = 0
        neighbors = get_neighbors(grid, i, j)
        for n_i, n_j in neighbors:
            if grid[n_i][n_j] == 1:
                DFS(n_i, n_j)
        
    nb_rows = len(grid)
    if nb_rows == 0:
        return 0
    nb_cols = len(grid[0])
    max_size = 0
    # Outer loop
    for i in range(nb_rows):
        for j in range(nb_cols):
            if grid[i][j] == 1:
                size = 0
                DFS(i, j) 
                if size > max_size:
                    max_size = size
    return max_size
    
def get_neighbors(grid, i, j):
    nb_rows = len(grid)
    if nb_rows == 0:
        return []
    nb_cols = len(grid[0])

    offset = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    output = []        
    for r, c in offset:
        n_i = i + r
        n_j = j + c
        if 0 <= n_i < nb_rows and 0 <= n_j < nb_cols:
            output.append((n_i, n_j))
    return output 
        
