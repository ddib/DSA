def get_binary_strings(n):
    """
    Problem:
    Given a number n, generate all possible binary strings of length n.

    Complexity:
    * Time: O(n * 2ˆn)
    * Space: O(n)
    """
  
    def helper(slate, i):
        if i == 0:
            result.append(slate)
            return
        helper(slate + "0", i - 1)
        helper(slate + "1", i - 1)
    
    result = []
    helper("", n)
    return result
