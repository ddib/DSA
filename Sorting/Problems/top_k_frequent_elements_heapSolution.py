import heapq
def find_top_k_frequent_elements(arr, k):
    """
    Problem:
    Given an integer array and a number k, find the k most frequent elements in the array.
    https://leetcode.com/problems/top-k-frequent-elements
    
    Complexity:
    * Time: O(nlog(k))
    * Space: O(n + k)
    """

    aux = {}
    n = len(arr)
    
    for i in range(n):
        aux[arr[i]] = aux.get(arr[i], 0) + 1
    
    m = len(aux)
  
    # Optimization 
    if m == k:
        return list(aux.keys())
    
    heap = []
    for (x1, x2) in aux.items():
        heapq.heappush(heap, (x2, x1))
        if len(heap) > k:
            heapq.heappop(heap)
        
    return [x[1] for x in heap]
