def heap_sort(arr):
    """
    Input: Array of comparables
    Output: Sorted array 
    Complexity:
     * Time: O(nlog(n))
     * Space: O(1) 
    Properties:
     * In-place
     * Stable (explanation: the heapification process makes sure that left child is always smaller than the right child)
    """
    n = len(arr)
    
    # Build heap
    bottom_node = n // 2 - 1
    for node in range(bottom_node, -1, -1):
        heapify(arr, node, n)
        
    # Sort heap
    for last_elt_index in range (n - 1, 0, -1):
        arr[0], arr[last_elt_index] = arr[last_elt_index], arr[0]
        heapify(arr, 0, last_elt_index)
    
    return arr


def heapify(arr, node, length):
    
    maxy = node
    left_child = 2 * node + 1
    right_child = 2 * node + 2
    if left_child < length and arr[left_child] > arr[maxy]:
        maxy = left_child
    if right_child < length and arr[right_child] > arr[maxy]:
        maxy = right_child
            
    if maxy != node:
        arr[maxy], arr[node] = arr[node], arr[maxy]
        heapify(arr, maxy, length)
