def convert_edge_list_to_adjacency_list(n, edges):
     """
    Problem:
    Convert the given edge list to the adjacency list of an undirected connected graph.
    An adjacency list represents a graph as a list of lists. The list index represents a vertex, and each element in its inner list represents the other vertices that form an edge with the vertex.

    Complexity:
    * Time: O(m + nlog(m)), n: number of vertices. m: number of edges.
    * Space: O(1)
    """

    output = [[] for _ in range(n)]
    
    for i, j in edges: # time complexity O(m)
        output[i].append(j)
        output[j].append(i)
    
    for adjacents in output: # time complexity O(nlog(m))
        adjacents.sort()
    return output
