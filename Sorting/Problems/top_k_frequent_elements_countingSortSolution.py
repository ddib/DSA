def find_top_k_frequent_elements(arr, k):
    """
    Problem:
    Given an integer array and a number k, find the k most frequent elements in the array.
    https://leetcode.com/problems/top-k-frequent-elements
    
    Complexity:
    * Time: O(n)
    * Space: O(n)
    """

    # get frequencies
    aux = {}
    n = len(arr)
    for i in arr:
        aux[i] = aux.get(i, 0) + 1
        
    # build Counting list
    counting_list = [[] for _ in range(n + 1)]
    
    for item in aux.keys():
        counting_list[aux[item]].append(item)
    
    # get result 
    result = []
    index = n
    while len(result) < k:
        result.extend(counting_list[index])
        index -= 1
        
    return result[:k]

    
        
        
        
        
