def online_median(stream):
    """
    Problem:
    Given a list of numbers, the task is to insert these numbers into a stream and find the median of the stream after each insertion. 
    If the median is a non-integer, consider it’s floor value.
    The median of a sorted array is defined as the middle element when the number of elements is odd and the mean of the middle two elements when the number of elements is even.
    (Variant of the problem): https://leetcode.com/problems/find-median-from-data-stream
    
    Complexity:
    * Time: O(n²)
    * Space: O(1)
    """
    n = len(stream)
    result = []
    for i in range(n):
        # insertion
        j = i - 1
        while j >= 0 and stream[j] > stream[j + 1]:
            stream[j + 1], stream[j] = stream[j], stream[j + 1]
            j -= 1
            
        # find median
        temp_n = i + 1
        if temp_n % 2 == 1:
            result.append(stream[temp_n // 2])
        else:
            result.append((stream[temp_n // 2] + stream[temp_n // 2 - 1]) // 2)
    return result
