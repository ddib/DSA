def bubble_sort(arr):
    """
    Input: Array of comparables
    Output: Sorted array 
    Complexity:
     * Time: O(n²)
     * Space: O(1) 
    Properties:
     * In-place
     * Not stable
    """
    n = len(arr)
    for i in range(n):
        is_swapped = False # Optimization 
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                is_swapped = True # Optimization 
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        if not is_swapped: # Optimization 
            break
            
    return arr
