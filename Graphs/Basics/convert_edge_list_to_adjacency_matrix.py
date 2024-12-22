def convert_edge_list_to_adjacency_matrix(n, edges):
    """
    Problem:
    Convert the given edge list to the adjacency matrix of an undirected connected graph.
    An adjacency matrix is a matrix with rows and columns labeled by graph vertices, 
    with a 1 or 0 in position (u, v) according to whether vertices u and v are adjacent or not.

    Complexity:
    * Time: O(m), n: number of vertices. m: number of edges.
    * Space: O(1)
    """
    
    output = [ [False] * n for _ in range(n) ]
    
    for i, j in edges: # time complexity O(m)
        output[i][j] = True
        output[j][i] = True
    
    return output
