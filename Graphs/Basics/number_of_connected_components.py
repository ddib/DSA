def number_of_connected_components(n, edges):
    """
    Problem:
    Given an undirected graph, find its total number of connected components.

    Input: number of nodes range(n), edge list
    Output: number of connected components
    
    Complexity:
    * Time: O(n + m), n: number of vertices. m: number of edges.
    * Space: O(n + m)

    Note: both BFS and DFS traversals solve this problem.
    """
  
    # 1- build the graph
    adjList = [ [] for _ in range(n)]
    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
        
    visited = [0] * n
    components = 0
    
    # 2- DFS
    def DFS(u):
        visited[u] = 1
        for v in adjList[u]:
            if visited[v] == 0:
                visited[v] = 1
                DFS(v)
    
    # 3- Outer loop
    for i in range(n):
        if visited[i] == 0:
            components += 1
            DFS(i)
            
    return components
