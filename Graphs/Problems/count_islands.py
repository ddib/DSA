def count_islands(matrix):
    """
    Problem:
    Given a two-dimensional matrix of 0s and 1s, find the number of islands.
    An island is a group of connected 1s or a standalone 1. 
    A cell in the matrix can be connected to up to 8 neighbors: 2 vertical, 2 horizontal and 4 diagonal.
    https://leetcode.com/problems/number-of-islands/description/
    
    Complexity:
    * Time: O(nb_rows * nb_cols)
    * Space: O(nb_rows * nb_cols)

    Note: both BFS and DFS traversals solve this problem.
    """
    
    def DFS_traversal(i, j):
        matrix[i][j] = 0
        neighbors = get_neighbors(matrix, i, j)
        for n_i, n_j in neighbors:
            if matrix[n_i][n_j] == 1:
                DFS_traversal(n_i, n_j)
        
    nb_rows = len(matrix)
    if nb_rows == 0:
        return 0
    nb_cols = len(matrix[0])

    # Outer loop 
    count = 0
    for i in range(nb_rows):
        for j in range(nb_cols):
            if matrix[i][j] == 1:
                count += 1
                DFS_traversal(i,j)
                        
    return count
    
def get_neighbors(matrix, i, j):
    nb_rows = len(matrix)
    if nb_rows == 0:
        return []
    nb_cols = len(matrix[0])
    output = []
    offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for r, c in offset:
        neighbor_i = i + r
        neighbor_j = j + c
        if 0 <= neighbor_i < nb_rows and 0 <= neighbor_j < nb_cols:
            output.append((neighbor_i, neighbor_j))
    return output 
