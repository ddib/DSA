undiscovered = -1
discovered = 0
completed = 1

def course_schedule(n, a, b):
    """
    Problem:
    A university has n courses to offer. To graduate from that university, a student must complete all those courses. 
    Some courses have prerequisite courses. One can take a course only after completing all of its prerequisites. 
    Dependencies between the courses are described by two arrays a and b of the same size: 
    course a[i] must be taken before course b[i] for all valid indices. 
    Is it possible to complete all the courses without violating constraints?
    https://leetcode.com/problems/course-schedule/description/

    Input: number of courses range(n), dependencies between courses in the two lists a[] and b[].
    Output: boolean
    
    Complexity:
    * Time: O(n + m)
    * Space: O(n + m)    
    """
    
    # Build the graph
    depList = [[] for _ in range(n)]
    for i in range(len(a)):
        depList[a[i]].append(b[i])
        
     
    # Cycle detection with DFS traversal    
    def DFS_cycle(node):
        state[node] = discovered
        for i in depList[node]:
            if state[i] == discovered:
                return True
            if state[i] == undiscovered:
                if DFS_cycle(i):
                    return True
        state[node] = completed
        return False


    # Outer loop
    state = [undiscovered] * n
    for node in range(n):
        if state[node] == undiscovered:
            if DFS_cycle(node):
                return False
    return True
