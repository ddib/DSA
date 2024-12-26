from collections import deque
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
        
    # BFS
    def BFS_bipartite(node, group):
        queue = deque()
        queue.append(node)
        visited[node] = group
        while queue:
            n = queue.popleft()
            g = visited[n]
            _g = 1 - g
            for i in graph[n]:
                if visited[i] == g:
                    return False
                if visited[i] == -1:
                    visited[i] = _g
                    queue.append(i)
        return True 
    
    # Outer loop
    visited = [-1] * n
    for node in range(n):
        if visited[node] == -1:
            if not BFS_bipartite(node, 0):
                return False
    
    return True
