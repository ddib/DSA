def count_all_subsets(n):
    """
    Problem:
    Given a number denoting the size of a set, count the number of unique subsets of that set.

    Complexity:
    * Time: O(n)
    * Space: O(n)
    """
    def helper(i):
        if i == 0:
            return 1
        return 2 * helper(i - 1)
      
    """
    Optimized helper
    
    Complexity:
    * Time: O(log(n))
    * Space: O(n)
    """
    def helperOpt(i):
        if i == 0:
            return 1
        
        odd = i % 2
        result = helperOpt(i // 2)
        result *= result
        if odd:
            result *= 2
        
        return result
  
    return helper(n)
#   return helperOpt(n)
