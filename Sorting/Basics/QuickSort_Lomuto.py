import random # Optional: to pick a random pivot number
def quick_sort(arr):
    """
    Lumuto's partitioning 
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
    if end <= start:
        return 

    # Optional: to pick a random pivot number
    pivot = random.randrange(start, end + 1)  
    arr[start], arr[pivot] = arr[pivot], arr[start]
    # # #
    
    smaller = start
    for bigger in range(start + 1, end + 1):
        if arr[bigger] <= arr[start]:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            
    arr[start], arr[smaller] = arr[smaller], arr[start]
    
    quick_sort_helper(arr, start, smaller - 1)
    quick_sort_helper(arr, smaller + 1, end)
    return 
