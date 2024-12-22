def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Problem:
    Given an undirected graph, find out whether it is a tree.
    A tree is an undirected connected acyclic graph.

    Input: number of nodes range(n), edges connect nodes edge_start and edge_end
    Output: boolean 
    
    Complexity:
    * Time: O(n + m), n: number of vertices. m: number of edges.
    * Space: O(n + m)

    Note: both BFS and DFS traversals solve this problem.
    """
  
    # Build the graph
    adjList = [[] for _ in range(node_count)]
    m = len(edge_start)
    
    for i in range(m):
        adjList[edge_start[i]].append(edge_end[i])
        adjList[edge_end[i]].append(edge_start[i])
        
    # DFS
    def DFS(node):
        for i in adjList[node]:
            if visited[i] == -1:
                visited[i] = node
                if not DFS(i):
                    return False
            else:
                if visited[node] != i:
                    return False
        return True
        
    # Outer loop
    components = 0
    visited = [-1] * node_count
    
    for i in range(node_count):
        if visited[i] == -1:
            visited[i] = None
            components += 1
            if components > 1:
                return False
            if not DFS(i):
                return False
    return True

