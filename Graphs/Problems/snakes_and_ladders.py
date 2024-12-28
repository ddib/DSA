from collections import deque
def minimum_number_of_rolls(n, moves):
    """
    Problem:
    Find the minimum number of die rolls necessary to reach the final cell of the given Snakes and Ladders board game.
    https://leetcode.com/problems/snakes-and-ladders/description/
    
    Input: number of nodes (n), array of integers (moves) defining the snakes and ladders (moves[i] = -1: no ladder or snake starts at i-th cell moves[i] = x: snake/ladder from i down/up to moves[i]).
    Output: int (number of rolls) 
    
    Complexity:
    * Time: O(n)
    * Space: O(n)
    """
    
    def get_neighbors(node):
        neighbors = []
        for i in range(1,7):
            neighbor = node + i
            if neighbor < n:
                if moves[neighbor] == -1:
                    neighbors.append(neighbor)
                else:
                    neighbors.append(moves[neighbor])
        return neighbors            
                    
    if n <= 1:
        return 0 
    
    # BFS
    visited = [False] * n #space: O(n)
    queue = deque() #space: O(n)
    queue.append((0, 0))
    while queue: #time: O(n)
        cell, roll = queue.popleft()
        if visited[cell]:
            continue
        visited[cell] = True
        neighbors = get_neighbors(cell) #time: O(1)
        for neighbor in neighbors: #time: O(1)
            if neighbor == n - 1:
                return roll + 1
            queue.append((neighbor, roll + 1))
    return -1
