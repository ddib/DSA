from collections import deque
base = 10

def radix_sort(arr):
    """
    Input: Array of integers
    Output: Sorted array 
    Complexity:
     * Time: O(n * d), d is the number of digits in the max element of the array 
     * Space: O(n) 
    Properties:
     * not in-place
     * Stable (doesn't apply for integers but can be stable when applied to objects)
     Note:
     * This solution uses the number system of base 10. 
     * A large number system base impacts the time and space complexities, where n -> (n + base).
     * Other number system bases have not been tested. 
    """
  
    # Find number of digits
    digits = len(str(max(arr)))

    # Perform series of counting sort
    for index in range(digits):
        arr = counting_sort(arr, index)

    return arr

def counting_sort(arr, index):
    count = [deque() for _ in range(base)]
    place = pow(base, index) 
    
    for element in arr:
        key = element // place
        count[key % base].append(element)

    arr = []
    for key in range(base):
        while count[key]:
            arr.append(count[key].popleft())
 
    return arr
