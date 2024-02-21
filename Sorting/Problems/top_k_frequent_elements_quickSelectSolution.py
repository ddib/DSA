def find_top_k_frequent_elements(arr, k):
    """
    Problem:
    Given an integer array and a number k, find the k most frequent elements in the array.
    https://leetcode.com/problems/top-k-frequent-elements
    
    Complexity:
    * Time: θ(n), O(n²)
    * Space: O(n)
    """

    # get frequencies O(n)
    aux = {}
    n = len(arr)
    
    for i in range(n):
        aux[arr[i]] = aux.get(arr[i], 0) + 1
    
    m = len(aux)
    
    # optimization 
    if m == k:
        return list(aux.keys())
    # # #
    
    aux = list(aux.items()) # O(n)
    quickselect_helper(aux, 0, m - 1, m - k)
        
    return [x[0] for x in aux[-k:]]


def quickselect_helper(aux, start, end, barrier):
    # Hoare partitioning 
    if end <= start:
        return
    
    smaller = start + 1
    bigger = end
   
    # get random pivot 
    pivot = random.randint(start, end)
    aux[pivot], aux[start] = aux[start], aux[pivot]
    # # #
    
    while smaller <= bigger:
        if aux[smaller][1] <= aux[start][1]:
            smaller += 1
        elif aux[bigger][1] > aux[start][1]:
            bigger -= 1
        else:
            aux[smaller], aux[bigger] = aux[bigger], aux[smaller]
            smaller += 1
            bigger -= 1
    aux[start], aux[bigger] = aux[bigger], aux[start]
    
    
    if bigger == barrier:
        return
    if bigger < barrier:
        quickselect_helper(aux, bigger + 1, end, barrier)
    else:
        quickselect_helper(aux, start, bigger - 1, barrier)
    
   
    
        
        
        
        
