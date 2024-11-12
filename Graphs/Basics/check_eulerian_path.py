def check_if_eulerian_path_exists(n, edges):
    """
    Problem:
    Given an undirected connected graph, check if any eulerian path exists in it. 
    The Eulerian Path is a path in the graph that visits every edge exactly once (allowing for revisiting vertices).

    Complexity:
    * Time: O(n + m)
    * Space: O(n)
    """

  if n <= 1:
        return True
  degrees = [0] * n
  for i, j in edges:
      degrees[i] += 1
      degrees[j] += 1
  
  even_degrees = 0
  for i in range(n):
      if degrees[i] % 2 == 1:
          even_degrees += 1
          if even_degrees > 2:
              return False
  if even_degrees == 1:
      return False

  return True
