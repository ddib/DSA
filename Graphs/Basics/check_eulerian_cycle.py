def check_if_eulerian_cycle_exists(n, edges):
    """
    Problem:
    Check an eulerian cycle exists in a given undirected connected graph. 
    The Euler cycle is a path in the graph that visits every edge exactly once and starts and finishes at the same vertex.

    Complexity:
    * Time: O(n + m)
    * Space: O(n)
    """
  
    if n <= 1:
        return True
    degrees = [0] * n # aux space of O(n)
    for i,j in edges: # time O(m)
        degrees[i] += 1
        degrees[j] += 1
    for i in range(n): # time O(n)
        if degrees[i] % 2 == 1:
            return False
    return True
