def two_sum(numbers, target):
    """
   Problem:
   Given an array and a target number, 
   find the indices of the two values from the array that sum up to the given target number.
   https://leetcode.com/problems/two-sum/

   Complexity:
    * Time: O(n)
    * Space: O(n) 

    """

    n = len(numbers)
    aux = {}
    
    for i in range(n):
        n1 = numbers[i]
        n2 = target - n1
        if n2 in aux:
            return [i, aux[n2]]
        aux[n1] = i
    return [-1, -1]
