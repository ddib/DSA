group1 = 0
group2 = 1
unsorted = -1
def friendly_groups(num_of_people, dislike1, dislike2):
    """
    Problem:
    There are n people living in a town. Some of them dislike each other. 
    Given the value of n and two equal integer arrays called dislike1 and dislike2. 
    For each i, the person dislike1[i] dislikes the person dislike2[i]. 
    Check if we can divide the people of the town into two sets such that each person belongs to exactly one set and no two persons disliking each other belong to the same set.

    Input: number of people, disliking pairs dislike1 and dislike2
    Output: boolean 
    
    Complexity:
    * Time: O(n + m), n: number of people. m: number of disliking pairs.
    * Space: O(n)
    """
    # Build the graph
    graph = [ [] for _ in range(num_of_people)]
    for i in range(len(dislike1)):
        graph[dislike1[i]].append(dislike2[i])
        graph[dislike2[i]].append(dislike1[i])
    
    # Sorting through DFS traversal
    def DFS_sorting(person, group):
        visited[person] = group
        other_group = (group + 1) % 2
        for i in graph[person]:
            if visited[i] == group:
                return False
            if visited[i] == unsorted:
                if not DFS_sorting(i, other_group):
                    return False
        return True
        
    # Outer loop   
    visited = [unsorted] * num_of_people
    for person in range(num_of_people):
        if visited[person] == unsorted:
            if not DFS_sorting(person, group1):
                return False
    return True
