
from collections import deque

def bfs_traversal(n, edges):
    """
    Problem:
    Given an undirected graph, perform a Breadth-First Search Traversal on it.

    Input: number of nodes range(n), edge list
    Output: BFS traversal of the graph
    
    Complexity:
    * Time: O(n + m), n: number of vertices. m: number of edges.
    * Space: O(n + m)
    """
  
    # Build the graph: edge list to adjacency list
    adjList = [ [] for _ in range(n)] # space O(n)
    for u, v in edges: # time O(m)
        adjList[u].append(v)
        adjList[v].append(u)
        
    # traverse the graph
    nodes = deque([ i for i in range(n)])
    captured = [0] * n
    output = []
    
    while nodes: # time O(n)
        # BFS traversal
        queue = deque()
        queue.append(nodes[0])
        while queue: # time O(m)
            u = queue.popleft()
            output.append(u)
            nodes.remove(u)
            captured[u] = 2
            for v in adjList[u]:
                if captured[v] == 0:
                    captured[v] = 1
                    queue.append(v)
                  
    return output
