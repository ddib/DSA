def insertion_sort(arr):
    """
    Input: Array of comparables
    Output: Sorted array 
    Complexity:
     * Time: O(n²)
     * Space: O(1) 
    Properties:
     * In-place
     * stable
    """
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr
