import heapq
def kth_largest(k, initial_stream, append_stream):
    """
    Problem:
    Given an initial list along with another list of numbers to be appended with the initial list and an integer k, 
    return an array of the k-th largest element after adding each element from the stream to the initial list.  
    https://leetcode.com/problems/kth-largest-element-in-a-stream/
    
    Complexity:
    * Time: O((n + m)log(k))
    * Space: O(k)
    """

    aux = []
    
    for element in initial_stream: #O(n)
        heapq.heappush(aux, element) #O(nlog(k))
        if len(aux) > k:
            heapq.heappop(aux)
            
    result = []
    for element in append_stream: #O(m)
        if element > aux[0] or len(aux) < k: # Optimization: to skip element less than the kth largest element when the heap size is k
          heapq.heappush(aux, element) #O(mlog(k))
          if len(aux) > k:
              heapq.heappop(aux)
        result.append(aux[0])
    return result
