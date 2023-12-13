def counting_sort(arr):
    """
    Input: Array of integers
    Output: Sorted array 
    Complexity:
     * Time: O(log(n + k)), k is the range of numbers in the array 
     * Space: O(k) 
    Properties:
     * not in-place
     * Stable (doesn't apply for integers but can be stable when applied to objects)
    """
    n = len(arr)
    aux = {}
    for i in range(n):
        key = arr[i]
        aux[key] = aux.get(key, 0) + 1
    
    min_key = min(arr)
    max_key = max(arr)

    arr = []
    for key in range(min_key, max_key + 1):
        if key in aux:
            frequency = aux[key]
            for i in range(frequency):
                arr.append(key)
    return arr
