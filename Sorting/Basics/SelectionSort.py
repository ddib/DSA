def selection_sort(arr):
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
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
