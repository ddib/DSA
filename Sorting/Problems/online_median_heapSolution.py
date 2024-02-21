import heapq
def online_median(stream):
    """
    Problem:
    Given a list of numbers, the task is to insert these numbers into a stream and find the median of the stream after each insertion. 
    If the median is a non-integer, consider it’s floor value.
    The median of a sorted array is defined as the middle element when the number of elements is odd and the mean of the middle two elements when the number of elements is even.
    (Variant of the problem): https://leetcode.com/problems/find-median-from-data-stream
    
    Complexity:
    * Time: O(nlog(n))
    * Space: O(n)
    """
    result = []
    min_heap = []
    max_heap = []
    
            
    for value in stream:
        if len(min_heap) == len(max_heap):
            heapq.heappush(max_heap, -heapq.heappushpop(min_heap, value))
            result.append(-max_heap[0])
        else:
            heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -value))
            result.append((min_heap[0] - max_heap[0]) // 2)
    
    
    return result
