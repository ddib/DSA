
def merge_sort(arr):
    """
    Input: Array of comparables
    Output: Sorted array 
    Complexity:
     * Time: O(nlog(n))
     * Space: O(n) 
    Properties:
     * Not in-place
     * Stable
    """

    merge_sort_helper(arr, 0, len(arr) - 1)
    return arr
    
def merge_sort_helper(arr, start, end):
    if start == end:
        return
    mid = start + ((end - start) // 2)
    merge_sort_helper(arr, start, mid)
    merge_sort_helper(arr, mid + 1, end)
    
    aux = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1
    if i <= mid:
        aux.extend(arr[i : mid + 1])
    if j <= end:
        aux.extend(arr[j : end + 1])
  
    arr[start : end + 1] = aux

    return
