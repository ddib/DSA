def kth_largest_in_an_array(arr, k):
    """
    Problem:
    Given an initial list along with another list of numbers to be appended with the initial list and an integer k, 
    return an array of the k-th largest element after adding each element from the stream to the initial list.  
    https://leetcode.com/problems/kth-largest-element-in-a-stream/
    
    Complexity:
    * Time: θ(n), O(n²)
    * Space: O(1)
    """

    n = len(arr)
    index = n - k
    quickselect_helper(arr, 0, n - 1, index)
    return arr[index]

def quickselect_helper(arr, start, end, index):
    # Lomuto partitioning 
    if start >= end:
        return 
    
    # get random pivot
    pivot = random.randint(start, end)
    arr[pivot], arr[start] = arr[start], arr[pivot]
    # # #
  
    smaller = start 
    for bigger in range(start + 1, end + 1):
        if arr[bigger] <= arr[start]:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            
    arr[start], arr[smaller]= arr[smaller], arr[start]
    
    if smaller == index:
        return
    if smaller < index:
        quickselect_helper(arr, smaller + 1, end, index)
    else:
        quickselect_helper(arr, start, smaller - 1, index)
    
