def find_top_k_frequent_elements(arr, k):
    """
    Problem:
    Given an integer array and a number k, find the k most frequent elements in the array.
    https://leetcode.com/problems/top-k-frequent-elements
    
    Complexity:
    * Time: O(nlog(n))
    * Space: O(n)
    """

    aux = {}
    n = len(arr)
    
    for i in range(n):
        aux[arr[i]] = aux.get(arr[i], 0) + 1
    
    m = len(aux)
  
    # Optimization 
    if m == k:
        return list(aux.keys())
    
    aux = sorted(aux.items(), key=lambda x: x[1])[m - k:]
        
    return [x[0] for x in aux]
