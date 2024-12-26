def is_bipartite(n, edges):
    """
    Problem:
    Check whether the given graph is bipartite or not?
    A graph is bipartite if the nodes can be partitioned into two independent sets, A and B, 
    such that every edge in the graph connects a node in set A and a node in set B.
    https://leetcode.com/problems/is-graph-bipartite/description/
    
    Input: number of nodes (n), edge list
    Output: boolean 
    
    Complexity:
    * Time: O(n + m), n: number of nodes. m: number of edges.
    * Space: O(n)
    """
  
    # Build the graph
    graph = [ [] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    # DFS
    def DFS_grouping(node, group):
        visited[node] = group
        other_group = (group + 1) % 2
        for i in graph[node]:
            if visited[i] == group:
                return False
            if visited[i] == -1:
                if not DFS_grouping(i, other_group):
                    return False
        return True
        
    # Outer loop
    visited = [-1] * n
    for node in range(n):
        if visited[node] == -1:
            if not DFS_grouping(node, 0):
                return False
    return True
