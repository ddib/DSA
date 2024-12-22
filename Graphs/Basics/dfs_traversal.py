def dfs_traversal(n, edges):
    """
    Problem:
    Given an undirected graph, perform a Depth-First Search Traversal on it.

    Input: number of nodes range(n), edge list
    Output: DFS traversal of the graph
    
    Complexity:
    * Time: O(n + m), n: number of vertices. m: number of edges.
    * Space: O(n + m)
    """
  
    # Build the graph: edge list to adjacency list
    adjList = [[] for _ in range(n)] # space O(n + m)
    for u, v in edges:  # time O(m)
        adjList[u].append(v)
        adjList[v].append(u)
    
    visited = [0] * n # space O(n)
    output = []
    
    def dfs_helper(u):
        visited[u] = 1
        output.append(u)
        for v in adjList[u]:
            if visited[v] == 0:
                dfs_helper(v)
    
    # Traverse the graph            
    for node in range(n): # time O(n)
        if visited[node] == 0:
            dfs_helper(node)  # time O(m)
            
    return output
