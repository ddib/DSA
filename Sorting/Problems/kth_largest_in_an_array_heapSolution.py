import heapq
def kth_largest_in_an_array(numbers, k):
    """
    Problem:
    Given an array of integers, find the k-th largest number in it.
    https://leetcode.com/problems/kth-largest-element-in-an-array

    Complexity:
    * Time: O(nlog(k))
    * Space: O(k)
    """
    
    aux = []
    
    for element in numbers:
      if len(aux) < k or element > aux[0]: # Optimization: to skip element less than the kth largest element when the heap size is k
          heapq.heappush(aux, element)
          if len(aux) > k:
              heapq.heappop(aux)
    return aux[0]
