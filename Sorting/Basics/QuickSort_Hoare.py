import random # Optional: to pick a random pivot number
def quick_sort(arr):
    """
    Hoare's partitioning 
    Input: Array of comparables
    Output: Sorted array 
    Complexity:
     * Time: θ(nlog(n)), O(n²)
     * Space: θ(log(n)), O(n) 
    Properties:
     * In-place
     * Not stable
    """
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr
    
def quick_sort_helper(arr, start, end):
    if start >= end:
        return

    # Optional: to pick a random pivot number
    pivot = random.randrange(start, end + 1)  
    arr[start], arr[pivot] = arr[pivot], arr[start]
    # # #

    smaller = start + 1
    bigger = end
    while smaller <= bigger:
        if arr[smaller] <= arr[start]:
            smaller += 1
        elif arr[bigger] > arr[start]:
            bigger -= 1
        else:
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            smaller += 1
            bigger -= 1
    arr[start], arr[bigger] = arr[bigger], arr[start]
    
    quick_sort_helper(arr, start, bigger - 1)
    quick_sort_helper(arr, bigger + 1, end)
    
    return
